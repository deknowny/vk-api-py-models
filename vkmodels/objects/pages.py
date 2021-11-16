import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


class PrivacySettings(int, enum.Enum):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2


@dataclasses.dataclass
class Wikipage(
    ObjectBase,
):
    group_id: int
    id: int
    title: str
    views: int
    who_can_edit: PrivacySettings
    who_can_view: PrivacySettings
    creator_id: typing.Optional[int] = None
    creator_name: typing.Optional[int] = None
    editor_id: typing.Optional[int] = None
    editor_name: typing.Optional[str] = None


@dataclasses.dataclass
class WikipageFull(
    ObjectBase,
):
    created: int
    edited: int
    group_id: int
    id: int
    title: str
    view_url: str
    views: int
    who_can_edit: PrivacySettings
    who_can_view: PrivacySettings
    creator_id: typing.Optional[int] = None
    current_user_can_edit: typing.Optional[BoolInt] = None
    current_user_can_edit_access: typing.Optional[BoolInt] = None
    editor_id: typing.Optional[int] = None
    html: typing.Optional[str] = None
    owner_id: typing.Optional[int] = None
    parent: typing.Optional[str] = None
    parent2: typing.Optional[str] = None
    source: typing.Optional[str] = None
    url: typing.Optional[str] = None


@dataclasses.dataclass
class WikipageHistory(
    ObjectBase,
):
    date: int
    editor_id: int
    editor_name: str
    id: int
    length: int
