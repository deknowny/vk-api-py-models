import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Product(
    ObjectBase,
):
    id: int
    type: str
    active: typing.Optional[BoolInt] = None
    has_animation: typing.Optional[bool] = None
    icon: typing.Optional[ProductIcon] = None
    is_new: typing.Optional[bool] = None
    payment_region: typing.Optional[str] = None
    previews: typing.Optional[typing.List[Image]] = None
    promoted: typing.Optional[BoolInt] = None
    purchase_date: typing.Optional[int] = None
    purchased: typing.Optional[BoolInt] = None
    stickers: typing.Optional[StickersList] = None
    style_sticker_ids: typing.Optional[typing.List[int]] = None
    subtitle: typing.Optional[str] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class StickersKeyword(
    ObjectBase,
):
    words: typing.List[str]

    promoted_stickers: typing.Optional[StickersKeywordStickers] = None
    stickers: typing.Optional[typing.List[StickersKeywordSticker]] = None
    user_stickers: typing.Optional[StickersList] = None


@dataclasses.dataclass
class StickersKeywordSticker(
    ObjectBase,
):
    pack_id: int
    sticker_id: int
