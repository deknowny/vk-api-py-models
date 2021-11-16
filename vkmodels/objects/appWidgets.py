import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Photo(
    ObjectBase,
):
    id: str
    images: typing.List[Image]


@dataclasses.dataclass
class Photos(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[Photo]] = None
