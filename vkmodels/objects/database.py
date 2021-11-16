import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Faculty(
    ObjectBase,
):
    id: typing.Optional[int] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class Region(
    ObjectBase,
):
    id: typing.Optional[int] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class School(
    ObjectBase,
):
    id: typing.Optional[int] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class Station(
    ObjectBase,
):
    id: int
    name: str
    city_id: typing.Optional[int] = None
    color: typing.Optional[str] = None


@dataclasses.dataclass
class University(
    ObjectBase,
):
    id: typing.Optional[int] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class City(
    ObjectBase,
    Object,
):
    area: typing.Optional[str] = None
    region: typing.Optional[str] = None
    important: typing.Optional[BoolInt] = None
