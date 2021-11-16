import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class DomainResolved(
    ObjectBase,
):
    group_id: typing.Optional[int] = None
    object_id: typing.Optional[int] = None
    type: typing.Optional[DomainResolvedType] = None


class DomainResolvedType(str, enum.Enum):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"


@dataclasses.dataclass
class LastShortenedLink(
    ObjectBase,
):
    access_key: typing.Optional[str] = None
    key: typing.Optional[str] = None
    short_url: typing.Optional[str] = None
    timestamp: typing.Optional[int] = None
    url: typing.Optional[str] = None
    views: typing.Optional[int] = None


@dataclasses.dataclass
class LinkChecked(
    ObjectBase,
):
    link: typing.Optional[str] = None
    status: typing.Optional[LinkCheckedStatus] = None


class LinkCheckedStatus(str, enum.Enum):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


@dataclasses.dataclass
class LinkStats(
    ObjectBase,
):
    key: typing.Optional[str] = None
    stats: typing.Optional[typing.List[Stats]] = None


@dataclasses.dataclass
class LinkStatsExtended(
    ObjectBase,
):
    key: typing.Optional[str] = None
    stats: typing.Optional[typing.List[StatsExtended]] = None


@dataclasses.dataclass
class ShortLink(
    ObjectBase,
):
    access_key: typing.Optional[str] = None
    key: typing.Optional[str] = None
    short_url: typing.Optional[str] = None
    url: typing.Optional[str] = None


@dataclasses.dataclass
class Stats(
    ObjectBase,
):
    timestamp: typing.Optional[int] = None
    views: typing.Optional[int] = None


@dataclasses.dataclass
class StatsCity(
    ObjectBase,
):
    city_id: typing.Optional[int] = None
    views: typing.Optional[int] = None


@dataclasses.dataclass
class StatsCountry(
    ObjectBase,
):
    country_id: typing.Optional[int] = None
    views: typing.Optional[int] = None


@dataclasses.dataclass
class StatsExtended(
    ObjectBase,
):
    cities: typing.Optional[typing.List[StatsCity]] = None
    countries: typing.Optional[typing.List[StatsCountry]] = None
    sex_age: typing.Optional[typing.List[StatsSexAge]] = None
    timestamp: typing.Optional[int] = None
    views: typing.Optional[int] = None


@dataclasses.dataclass
class StatsSexAge(
    ObjectBase,
):
    age_range: typing.Optional[str] = None
    female: typing.Optional[int] = None
    male: typing.Optional[int] = None
