import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class App(
    ObjectBase,
    AppMin,
):
    author_url: typing.Optional[str] = None
    banner_1120: typing.Optional[str] = None
    banner_560: typing.Optional[str] = None
    icon_16: typing.Optional[str] = None
    is_new: typing.Optional[BoolInt] = None
    push_enabled: typing.Optional[BoolInt] = None
    screen_orientation: typing.Optional[int] = None
    friends: typing.Optional[typing.List[int]] = None
    catalog_position: typing.Optional[int] = None
    description: typing.Optional[str] = None
    genre: typing.Optional[str] = None
    genre_id: typing.Optional[int] = None
    international: typing.Optional[bool] = None
    is_in_catalog: typing.Optional[int] = None
    leaderboard_type: typing.Optional[AppLeaderboardType] = None
    members_count: typing.Optional[int] = None
    platform_id: typing.Optional[str] = None
    published_date: typing.Optional[int] = None
    screen_name: typing.Optional[str] = None
    section: typing.Optional[str] = None


class AppLeaderboardType(int, enum.Enum):
    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2


@dataclasses.dataclass
class AppMin(
    ObjectBase,
):
    id: int
    title: str
    type: AppType
    author_owner_id: typing.Optional[int] = None
    background_loader_color: typing.Optional[str] = None
    icon_139: typing.Optional[str] = None
    icon_150: typing.Optional[str] = None
    icon_278: typing.Optional[str] = None
    icon_576: typing.Optional[str] = None
    icon_75: typing.Optional[str] = None
    is_installed: typing.Optional[bool] = None
    loader_icon: typing.Optional[str] = None


class AppType(str, enum.Enum):
    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


@dataclasses.dataclass
class CatalogList(
    ObjectBase,
):
    count: int
    items: typing.List[App]

    profiles: typing.Optional[typing.List[UserMin]] = None


@dataclasses.dataclass
class Leaderboard(
    ObjectBase,
):
    user_id: int
    level: typing.Optional[int] = None
    points: typing.Optional[int] = None
    score: typing.Optional[int] = None


@dataclasses.dataclass
class Scope(
    ObjectBase,
):
    name: str
    title: typing.Optional[str] = None
