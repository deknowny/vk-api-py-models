import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Audio(
    ObjectBase,
):
    artist: str
    duration: int
    id: int
    owner_id: int
    title: str
    access_key: typing.Optional[str] = None
    album_id: typing.Optional[int] = None
    date: typing.Optional[int] = None
    genre_id: typing.Optional[int] = None
    performer: typing.Optional[str] = None
    url: typing.Optional[str] = None
