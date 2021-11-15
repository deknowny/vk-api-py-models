# WARNING: shitcode
from __future__ import annotations

import dataclasses
import pathlib
import json
import typing
import urllib.parse

from codegen.snake2pascal import snake2pascal


_cached_stores = {}


@dataclasses.dataclass
class ProxyBase:

    view: list | dict
    base_path: pathlib.Path

    def __contains__(self, item):
        return item in self.view

    def __setitem__(self, key, value):
        return self.view.__setitem__(key, value)

    def __getitem__(self, item) -> typing.Any:
        new_value = self.view[item]
        if isinstance(new_value, dict):
            ref = None
            if "$ref" in new_value:
                ref = JSONObjectReference.from_ref_obj(
                    base_path=self.base_path,
                    obj=new_value
                )
                new_value = ref.source
            return JSONObjectProxy(
                view=new_value,
                base_path=self.base_path,
                reference=ref
            )
        elif isinstance(new_value, list):
            return JSONArrayProxy(
                view=new_value,
                base_path=self.base_path
            )

        return new_value

    def __len__(self):
        return len(self.view)

    def __iter_(self):
        return iter(self.view)



@dataclasses.dataclass
class JSONObjectReference:
    filename: str
    keys_path: tuple[str]
    model_name: str
    source: typing.Any

    @classmethod
    def from_ref_obj(cls, obj: dict, base_path: pathlib.Path) -> JSONObjectReference:
        uri = obj.pop("$ref")
        parsed_uri = urllib.parse.urlparse(uri)
        another_schema = _cached_stores.get(
            parsed_uri.path,
            json.load(
                (base_path.parent / parsed_uri.path).open()
            )
        )
        _cached_stores[parsed_uri.path] = another_schema
        another_schema_keys = parsed_uri.fragment.removeprefix("/").split("/")
        source = another_schema
        for key in another_schema_keys:
            source = source[key]

        source.update(obj)
        if "$ref" in source:
            return cls.from_ref_obj(source, base_path)

        return cls(
            source=source,
            keys_path=another_schema_keys,
            filename=parsed_uri.path,
            model_name=snake2pascal(another_schema_keys[-1].split("_", 1)[1])
        )



@dataclasses.dataclass
class JSONObjectProxy(ProxyBase):
    reference: typing.Optional[JSONObjectReference] = None

    @classmethod
    def from_potential_ref(cls, obj, base_path):
        ref = None
        if "$ref" in obj:
            ref = JSONObjectReference.from_ref_obj(
                base_path=base_path,
                obj=obj
            )
            obj = ref.source
        return cls(
            view=obj,
            base_path=base_path,
            reference=ref
        )

    def items(self):
        yield from [
            (k, self[k]) for k in self.view
        ]

    def get(self, item, replacer=None):
        return self.view.get(item, replacer)



@dataclasses.dataclass
class JSONArrayProxy(ProxyBase):
    pass



def load_json_schema(path: pathlib.Path) -> JSONObjectProxy:
    json_schema = json.load(path.open())
    if isinstance(json_schema, dict):
        return JSONObjectProxy(
            view=json_schema,
            base_path=path
        )
    else:
        raise ValueError("Can't parse json schema only with reference")