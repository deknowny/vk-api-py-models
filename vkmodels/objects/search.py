import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Hint(
    ObjectBase,
):
    description: str
    type: HintType
    app: typing.Optional[App] = None
    field_global: typing.Optional[BoolInt] = None
    group: typing.Optional[Group] = None
    link: typing.Optional[Link] = None
    profile: typing.Optional[UserMin] = None
    section: typing.Optional[HintSection] = None


class HintSection(str, enum.Enum):
    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"
    PROMO = "promo"


class HintType(str, enum.Enum):
    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"
    LINK = "link"
