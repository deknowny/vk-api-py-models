import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Currency(
    ObjectBase,
):
    id: int
    name: str
    title: str


@dataclasses.dataclass
class MarketAlbum(
    ObjectBase,
):
    count: int
    id: int
    owner_id: int
    title: str
    updated_time: int
    is_hidden: typing.Optional[bool] = None
    is_main: typing.Optional[bool] = None
    photo: typing.Optional[Photo] = None


@dataclasses.dataclass
class MarketCategory(
    ObjectBase,
):
    id: int
    name: str
    section: Section


@dataclasses.dataclass
class MarketCategoryNested(
    ObjectBase,
):
    id: int
    name: str
    parent: typing.Optional[MarketCategoryNested] = None


@dataclasses.dataclass
class MarketCategoryOld(
    ObjectBase,
):
    id: int
    name: str
    section: Section


@dataclasses.dataclass
class MarketCategoryTree(
    ObjectBase,
):
    id: int
    name: str
    children: typing.Optional[typing.List[MarketCategoryTree]] = None


@dataclasses.dataclass
class MarketItem(
    ObjectBase,
):
    availability: MarketItemAvailability
    category: MarketCategoryOld
    description: str
    id: int
    owner_id: int
    price: Price
    title: str
    access_key: typing.Optional[str] = None
    button_title: typing.Optional[str] = None
    date: typing.Optional[int] = None
    external_id: typing.Optional[str] = None
    is_favorite: typing.Optional[bool] = None
    is_main_variant: typing.Optional[bool] = None
    sku: typing.Optional[str] = None
    thumb_photo: typing.Optional[str] = None
    url: typing.Optional[str] = None
    variants_grouping_id: typing.Optional[int] = None


class MarketItemAvailability(int, enum.Enum):
    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2


@dataclasses.dataclass
class MarketItemFull(
    ObjectBase,
    MarketItem,
):
    albums_ids: typing.Optional[typing.List[int]] = None
    photos: typing.Optional[typing.List[Photo]] = None
    can_comment: typing.Optional[BoolInt] = None
    can_repost: typing.Optional[BoolInt] = None
    likes: typing.Optional[Likes] = None
    reposts: typing.Optional[RepostsInfo] = None
    views_count: typing.Optional[int] = None
    wishlist_item_id: typing.Optional[int] = None
    cancel_info: typing.Optional[Link] = None
    user_agreement_info: typing.Optional[str] = None


@dataclasses.dataclass
class Order(
    ObjectBase,
):
    date: int
    group_id: int
    id: int
    items_count: int
    status: int
    total_price: Price
    user_id: int
    address: typing.Optional[str] = None
    cancel_info: typing.Optional[Link] = None
    comment: typing.Optional[str] = None
    display_order_id: typing.Optional[str] = None
    merchant_comment: typing.Optional[str] = None
    preview_order_items: typing.Optional[typing.List[OrderItem]] = None
    track_link: typing.Optional[str] = None
    track_number: typing.Optional[str] = None
    weight: typing.Optional[int] = None


@dataclasses.dataclass
class OrderItem(
    ObjectBase,
):
    item: MarketItem
    item_id: int
    owner_id: int
    price: Price
    quantity: int
    photo: typing.Optional[Photo] = None
    title: typing.Optional[str] = None
    variants: typing.Optional[typing.List[str]] = None


@dataclasses.dataclass
class Price(
    ObjectBase,
):
    amount: str
    currency: Currency
    text: str
    discount_rate: typing.Optional[int] = None
    old_amount: typing.Optional[str] = None
    old_amount_text: typing.Optional[str] = None


@dataclasses.dataclass
class Section(
    ObjectBase,
):
    id: int
    name: str


class ServicesViewType(int, enum.Enum):
    CARDS = 1
    ROWS = 2
