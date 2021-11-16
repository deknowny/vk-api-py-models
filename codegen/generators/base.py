import abc
import dataclasses
import json
import pathlib
import typing

from codegen.loader import load_json_schema

GeneratorType = typing.TypeVar("GeneratorType")


@dataclasses.dataclass
class GeneratorBase(abc.ABC):
    schema_filename: typing.ClassVar[str]

    schema: dict
    schema_path: pathlib.Path
    models_path: pathlib.Path

    @abc.abstractmethod
    def run_codegen(self) -> None:
        pass

    @classmethod
    def fetch(
        cls: typing.Type[GeneratorType],
        schema_path: pathlib.Path,
        models_path: pathlib.Path,
    ) -> GeneratorType:
        schema_path /= cls.schema_filename
        schema = json.load(schema_path.open())
        return cls(
            schema=schema, schema_path=schema_path, models_path=models_path
        )
