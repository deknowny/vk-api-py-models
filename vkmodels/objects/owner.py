import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class State(
    ObjectBase,
):
    description: typing.Optional[str] = None
    state: typing.Optional[int] = None
