import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class GiveEventStickerItem(
    ObjectBase,
):
    status: typing.Optional[str] = None
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class Level(
    ObjectBase,
):
    level: typing.Optional[int] = None
    uid: typing.Optional[int] = None


@dataclasses.dataclass
class SmsNotification(
    ObjectBase,
):
    app_id: typing.Optional[str] = None
    date: typing.Optional[str] = None
    id: typing.Optional[str] = None
    message: typing.Optional[str] = None
    user_id: typing.Optional[str] = None


@dataclasses.dataclass
class TokenChecked(
    ObjectBase,
):
    date: typing.Optional[int] = None
    expire: typing.Optional[int] = None
    success: typing.Optional[int] = 1
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class Transaction(
    ObjectBase,
):
    date: typing.Optional[int] = None
    id: typing.Optional[int] = None
    uid_from: typing.Optional[int] = None
    uid_to: typing.Optional[int] = None
    votes: typing.Optional[int] = None
