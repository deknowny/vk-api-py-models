import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Status(
    ObjectBase,
):
    text: str
    audio: typing.Optional[Audio] = None
