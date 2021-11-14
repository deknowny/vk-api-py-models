from __future__ import annotations

import collections
import dataclasses
import pathlib
import threading
import typing

import jinja2

from codegen.generators.base import GeneratorBase
from codegen.loader import Reference
from codegen.snake2pascal import snake2pascal

ObjectsType: typing.TypeAlias = dict[str, dict]


class ObjectsGenerator(GeneratorBase):

    schema_filename: typing.ClassVar[str] = "objects.json"

    def run_codegen(self) -> None:
        objects_path, objects = self._fetch_objects()
        template_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                pathlib.Path("codegen") / "templates" / "objects"
            )
        )
        gen_threads = []
        for key, value in objects.items():
            template = template_env.get_template("main.py.jinja")
            thread = threading.Thread(
                target=lambda: self._gen_section(key, value, objects_path, template)
            )
            gen_threads.append(thread)
            thread.start()

        for thread in gen_threads:
            thread.join()

    def _gen_section(
        self,
        key: str,
        value: dict,
        objects_path: pathlib.Path,
        template: jinja2.Template
    ):
        filename = objects_path / f"{key}.py"
        filename.touch()
        template.stream(
            objects_data=value,
            reference_type=Reference,
            snake2pascal=snake2pascal,
            isinstance=isinstance,
            print=print,
            zip=zip
        ).dump(filename.open(mode="w"))

    def _fetch_objects(self) -> tuple[pathlib.Path, ObjectsType]:
        objects_path = self.models_path / "objects"
        objects_path.mkdir()
        ordinaries = collections.defaultdict(dict)
        for key, value in self.schema["definitions"].items():
            key_prefix, ordinary_name = key.split("_", 1)
            ordinary_name = snake2pascal(ordinary_name)
            ordinaries[key_prefix][ordinary_name] = value
            if not isinstance(value, Reference) and "properties" in value:
                value["properties"] = dict(
                    sorted(
                        value["properties"].items(),
                        key=lambda pair: (pair[0] not in value.get("required", []), pair[0])
                    )
                )

        return objects_path, ordinaries

