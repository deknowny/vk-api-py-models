from __future__ import annotations

import collections
import dataclasses
import itertools
import pathlib
import threading
import typing

import jinja2
from codegen.generators.base import GeneratorBase
from codegen.loader import JSONObjectProxy
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
                target=lambda: self._gen_section(
                    key, value, objects_path, template
                )
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
        template: jinja2.Template,
    ):
        filename = objects_path / f"{key}.py"
        filename.touch()
        template.stream(
            objects_data=value,
            snake2pascal=snake2pascal,
            isinstance=isinstance,
            print=print,
            zip=zip,
            list=list,
            json_object_proxy=JSONObjectProxy,
        ).dump(filename.open(mode="w"))

    def _fetch_objects(self) -> tuple[pathlib.Path, ObjectsType]:
        objects_path = self.models_path / "objects"
        objects_path.mkdir()
        ordinaries = collections.defaultdict(dict)

        # Models data sorting
        for key, value in self.schema["definitions"].items():
            key_prefix, ordinary_name = key.split("_", 1)
            ordinary_name = snake2pascal(ordinary_name)
            ordinaries[key_prefix][ordinary_name] = value
            value["toEnd"] = 0

            # Reorder model fields to pretend from case
            # Where optional is before required

            proxy_dict = JSONObjectProxy.from_potential_ref(
                value, self.schema_path
            )
            if proxy_dict.reference is None and "properties" in value:
                value["properties"] = dict(
                    sorted(
                        value["properties"].items(),
                        key=lambda pair: (
                            pair[0] not in value.get("required", []),
                            pair[0],
                        ),
                    )
                )
            if check_list := value.get("allOf") or value.get("oneOf"):
                for parent in check_list:
                    proxy_parent = JSONObjectProxy.from_potential_ref(
                        parent, base_path=self.schema_path
                    )
                    if proxy_parent.reference is not None and (
                        proxy_parent.reference.model_name
                        not in ordinaries[key_prefix]
                        or ordinaries[key_prefix][
                            proxy_parent.reference.model_name
                        ]["toEnd"]
                    ):
                        ordinaries[key_prefix][ordinary_name]["toEnd"] += 1

        # Reorder for correct inheritance
        for section, models in ordinaries.items():
            ordinaries[section] = dict(
                sorted(models.items(), key=lambda pair: pair[1]["toEnd"])
            )

        return objects_path, JSONObjectProxy.from_potential_ref(
            ordinaries, self.schema_path
        )
