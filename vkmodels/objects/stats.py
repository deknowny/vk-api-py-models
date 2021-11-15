import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Activity(
    ObjectBase,
):
    comments: typing.Optional[int] = None
    copies: typing.Optional[int] = None
    hidden: typing.Optional[int] = None
    likes: typing.Optional[int] = None
    subscribed: typing.Optional[int] = None
    unsubscribed: typing.Optional[int] = None


@dataclasses.dataclass
class City(
    ObjectBase,
):
    count: typing.Optional[int] = None
    name: typing.Optional[str] = None
    value: typing.Optional[int] = None


@dataclasses.dataclass
class Country(
    ObjectBase,
):
    code: typing.Optional[str] = None
    count: typing.Optional[int] = None
    name: typing.Optional[str] = None
    value: typing.Optional[int] = None


@dataclasses.dataclass
class Period(
    ObjectBase,
):
    activity: typing.Optional[Activity] = None
    period_from: typing.Optional[int] = None
    period_to: typing.Optional[int] = None
    reach: typing.Optional[Reach] = None
    visitors: typing.Optional[Views] = None


@dataclasses.dataclass
class Reach(
    ObjectBase,
):
    age: typing.Optional[typing.List[SexAge]] = None
    cities: typing.Optional[typing.List[City]] = None
    countries: typing.Optional[typing.List[Country]] = None
    mobile_reach: typing.Optional[int] = None
    reach: typing.Optional[int] = None
    reach_subscribers: typing.Optional[int] = None
    sex: typing.Optional[typing.List[SexAge]] = None
    sex_age: typing.Optional[typing.List[SexAge]] = None


@dataclasses.dataclass
class SexAge(
    ObjectBase,
):
    value: str
    count: typing.Optional[int] = None
    count_subscribers: typing.Optional[int] = None
    reach: typing.Optional[int] = None
    reach_subscribers: typing.Optional[int] = None


@dataclasses.dataclass
class Views(
    ObjectBase,
):
    age: typing.Optional[typing.List[SexAge]] = None
    cities: typing.Optional[typing.List[City]] = None
    countries: typing.Optional[typing.List[Country]] = None
    mobile_views: typing.Optional[int] = None
    sex: typing.Optional[typing.List[SexAge]] = None
    sex_age: typing.Optional[typing.List[SexAge]] = None
    views: typing.Optional[int] = None
    visitors: typing.Optional[int] = None


@dataclasses.dataclass
class WallpostStat(
    ObjectBase,
):
    hide: typing.Optional[int] = None
    join_group: typing.Optional[int] = None
    links: typing.Optional[int] = None
    post_id: typing.Optional[int] = None
    reach_ads: typing.Optional[int] = None
    reach_subscribers: typing.Optional[int] = None
    reach_subscribers_count: typing.Optional[int] = None
    reach_total: typing.Optional[int] = None
    reach_total_count: typing.Optional[int] = None
    reach_viral: typing.Optional[int] = None
    report: typing.Optional[int] = None
    sex_age: typing.Optional[typing.List[SexAge]] = None
    to_group: typing.Optional[int] = None
    unsubscribe: typing.Optional[int] = None
