import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class GetAdCategoriesResponseCategoriesCategory(
    ObjectBase,
):
    id: int
    name: str


@dataclasses.dataclass
class GetAdUnitsResponseAdUnitsAdUnit(
    ObjectBase,
):
    id: int
    site_id: int
    name: typing.Optional[str] = None


@dataclasses.dataclass
class GetFraudHistoryResponseEntriesEntry(
    ObjectBase,
):
    day: str
    site_id: int


@dataclasses.dataclass
class GetSitesResponseSitesSite(
    ObjectBase,
):
    id: int
    domains: typing.Optional[str] = None
    status_moder: typing.Optional[str] = None
    status_user: typing.Optional[str] = None


@dataclasses.dataclass
class GetStatisticsResponseItemsItem(
    ObjectBase,
):
    ad_unit_id: typing.Optional[int] = None
    day_max: typing.Optional[str] = None
    day_min: typing.Optional[str] = None
    days_count: typing.Optional[int] = None
    hour_max: typing.Optional[str] = None
    hour_min: typing.Optional[str] = None
    hours_count: typing.Optional[int] = None
    month_max: typing.Optional[str] = None
    month_min: typing.Optional[str] = None
    months_count: typing.Optional[int] = None
    overall_count: typing.Optional[int] = None
    site_id: typing.Optional[int] = None
