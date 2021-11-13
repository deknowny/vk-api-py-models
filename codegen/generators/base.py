import abc
import dataclasses
import pathlib
import typing

import jsonref

from codegen.loader import load_json

GeneratorType = typing.TypeVar("GeneratorType")


@dataclasses.dataclass
class GeneratorBase(abc.ABC):
    schema_filename: typing.ClassVar[str]

    schema: dict
    models_path: pathlib.Path

    @abc.abstractmethod
    def run_codegen(self) -> None:
        pass

    @classmethod
    def fetch(cls: typing.Type[GeneratorType], models_path: pathlib.Path) -> GeneratorType:
        path = pathlib.Path("vk-api-schema") / cls.schema_filename
        schema = load_json(path)
        return cls(schema=schema, models_path=models_path)


