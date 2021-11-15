import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Cover(
    ObjectBase,
):
    sizes: typing.Optional[typing.List[PhotoSizes]] = None


@dataclasses.dataclass
class ExternalData(
    ObjectBase,
):
    cover: typing.Optional[Cover] = None
    owner_name: typing.Optional[str] = None
    owner_url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    url: typing.Optional[str] = None
