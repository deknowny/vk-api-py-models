import abc
import dataclasses
import pathlib
import typing

from codegen.loader import load_json_schema

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
        schema = load_json_schema(path)
        return cls(schema=schema, models_path=models_path)


