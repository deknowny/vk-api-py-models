from __future__ import annotations

import dataclasses
import pathlib

import json
import typing
import urllib.parse


_cached_stores = {}


@dataclasses.dataclass
class Reference(typing.Mapping):

    original: dict
    uri: str

    def __getitem__(self, item):
        return self.original[item]

    def __len__(self):
        return len(self.original)

    def __iter__(self):
        return iter(self.original)

    @classmethod
    def resolve(cls, uri: str, base_path: pathlib.Path) -> Reference:
        parsed_uri = urllib.parse.urlparse(uri)
        another_schema = _cached_stores.get(
            parsed_uri.path,
            json.load(
                (base_path.parent / parsed_uri.path).open()
            )
        )
        another_schema_keys = parsed_uri.fragment.removeprefix("/").split("/")
        original = another_schema
        for key in another_schema_keys:
            original = original[key]

        return cls(
            original=original,
            uri=uri
        )


def _object_hook(base_path: pathlib.Path) -> typing.Callable[[dict], typing.Any]:
    def _object_hook_logic(obj: dict) -> Reference | dict:
        first_key = list(obj.keys())[0]
        if first_key == "$ref":
            return Reference.resolve(obj[first_key], base_path)
        return obj
    return _object_hook_logic


def load_json(path: pathlib.Path) -> dict:
    return json.load(path.open(), object_hook=_object_hook(path))