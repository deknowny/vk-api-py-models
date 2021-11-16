import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Value(
    ObjectBase,
):
    key: str
    value: str
