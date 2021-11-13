from __future__ import annotations

import collections
import dataclasses
import pathlib
import threading
import typing

import jinja2

from codegen.generators.base import GeneratorBase
from codegen.snake2camel import snake2camel

ObjectsType: typing.TypeAlias = dict[str, dict]


class ObjectsGenerator(GeneratorBase):

    schema_filename: typing.ClassVar[str] = "objects.json"

    def run_codegen(self) -> None:
        objects_path, objects = self._fetch_objects()
        template_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                pathlib.Path("codegen") / "templates"
            )
        )
        gen_threads = []
        for key, value in objects.items():
            template = template_env.get_template("objects.py.jinja")
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
            class_name="Test"
        ).dump(filename.open(mode="w"))

    def _fetch_objects(self) -> tuple[pathlib.Path, ObjectsType]:
        objects_path, objects = self._init_objects()
        for section, value in objects.items():
            file_path = objects_path / f"{section}.py"
            value["path"] = file_path

        return objects_path, objects

    def _init_objects(self) -> tuple[pathlib.Path, ObjectsType]:
        objects_path = self.models_path / "objects"
        objects_path.mkdir()
        ordinaries = collections.defaultdict(dict)
        for key, value in self.schema["definitions"].items():
            key_prefix, ordinary_name = key.split("_", 1)
            ordinary_name = snake2camel(ordinary_name)
            ordinaries[key_prefix][ordinary_name] = value

        return objects_path, ordinaries

