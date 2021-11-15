import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Bookmark(
    ObjectBase,
):
    added_date: int
    seen: bool
    tags: typing.List[Tag]

    type: BookmarkType
    link: typing.Optional[Link] = None
    post: typing.Optional[WallpostFull] = None
    product: typing.Optional[MarketItem] = None
    video: typing.Optional[Video] = None


class BookmarkType(str, enum.Enum):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"


@dataclasses.dataclass
class Page(
    ObjectBase,
):
    description: str
    tags: typing.List[Tag]

    type: PageType
    group: typing.Optional[GroupFull] = None
    updated_date: typing.Optional[int] = None
    user: typing.Optional[UserFull] = None


class PageType(str, enum.Enum):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"


@dataclasses.dataclass
class Tag(
    ObjectBase,
):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
