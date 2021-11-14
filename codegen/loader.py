from __future__ import annotations

import dataclasses
import pathlib
import json
import typing
import urllib.parse

from codegen.snake2pascal import snake2pascal



_cached_stores = {}


@dataclasses.dataclass
class Reference(typing.Mapping):

    original: dict
    uri: str
    last_key: str
    model_name: str

    def __getitem__(self, item):
        return self.original[item]

    def __len__(self):
        return len(self.original)

    def __iter__(self):
        return iter(self.original)

    @classmethod
    def resolve(cls, obj: str, base_path: pathlib.Path) -> Reference:
        uri = obj["$ref"]
        parsed_uri = urllib.parse.urlparse(uri)
        another_schema = _cached_stores.get(
            parsed_uri.path,
            json.load(
                (base_path.parent / parsed_uri.path).open()
            )
        )
        _cached_stores[parsed_uri.path] = another_schema
        another_schema_keys = parsed_uri.fragment.removeprefix("/").split("/")

        original = another_schema
        for key in another_schema_keys:
            original = original[key]

        _replace_references(original, base_path)
        return cls(
            original=original,
            uri=uri,
            last_key=another_schema_keys[-1],
            model_name=snake2pascal(another_schema_keys[-1].split("_", 1)[1])
        )


def _replace_references(obj, base_path):
    hook = _object_hook(base_path)
    for key, value in obj.items():
        if isinstance(value, dict):
            new_value = hook(value)
            if isinstance(new_value, dict):
                print(key, type(new_value))
                new_value = _replace_references(value, base_path)
            obj[key] = new_value

    return obj



def _object_hook(base_path: pathlib.Path) -> typing.Callable[[dict], typing.Any]:
    def _object_hook_logic(obj: dict) -> Reference | dict:
        if "$ref" in obj:
            return Reference.resolve(obj, base_path)
        return obj
    return _object_hook_logic


def load_json(path: pathlib.Path) -> dict:
    return json.load(path.open(), object_hook=_object_hook(path))