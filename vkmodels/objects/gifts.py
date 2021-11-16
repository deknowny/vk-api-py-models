import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Gift(
    ObjectBase,
):
    date: typing.Optional[int] = None
    from_id: typing.Optional[int] = None
    gift: typing.Optional[Layout] = None
    gift_hash: typing.Optional[str] = None
    id: typing.Optional[int] = None
    message: typing.Optional[str] = None
    privacy: typing.Optional[GiftPrivacy] = None


class GiftPrivacy(int, enum.Enum):
    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


@dataclasses.dataclass
class Layout(
    ObjectBase,
):
    build_id: typing.Optional[str] = None
    id: typing.Optional[int] = None
    is_stickers_style: typing.Optional[bool] = None
    keywords: typing.Optional[str] = None
    stickers_product_id: typing.Optional[int] = None
    thumb_256: typing.Optional[str] = None
    thumb_48: typing.Optional[str] = None
    thumb_512: typing.Optional[str] = None
    thumb_96: typing.Optional[str] = None
