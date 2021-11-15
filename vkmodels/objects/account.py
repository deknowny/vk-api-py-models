import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class AccountCounters(
    ObjectBase,
):
    app_requests: typing.Optional[int] = None
    events: typing.Optional[int] = None
    faves: typing.Optional[int] = None
    friends: typing.Optional[int] = None
    friends_recommendations: typing.Optional[int] = None
    friends_suggestions: typing.Optional[int] = None
    gifts: typing.Optional[int] = None
    groups: typing.Optional[int] = None
    memories: typing.Optional[int] = None
    menu_clips_badge: typing.Optional[int] = None
    menu_discover_badge: typing.Optional[int] = None
    messages: typing.Optional[int] = None
    notes: typing.Optional[int] = None
    notifications: typing.Optional[int] = None
    photos: typing.Optional[int] = None
    sdk: typing.Optional[int] = None


@dataclasses.dataclass
class Info(
    ObjectBase,
):
    field_2fa_required: typing.Optional[BoolInt] = None
    country: typing.Optional[str] = None
    https_required: typing.Optional[BoolInt] = None
    intro: typing.Optional[BoolInt] = None
    lang: typing.Optional[int] = None
    link_redirects: typing.Optional[dict] = None
    mini_apps_ads_slot_id: typing.Optional[int] = None
    no_wall_replies: typing.Optional[BoolInt] = None
    own_posts_default: typing.Optional[BoolInt] = None
    qr_promotion: typing.Optional[int] = None
    show_vk_apps_intro: typing.Optional[bool] = None
    subscriptions: typing.Optional[Subscriptions] = None
    wishlists_ae_promo_banner_show: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class NameRequest(
    ObjectBase,
):
    first_name: typing.Optional[str] = None
    id: typing.Optional[int] = None
    lang: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    link_href: typing.Optional[str] = None
    link_label: typing.Optional[str] = None
    status: typing.Optional[NameRequestStatus] = None


class NameRequestStatus(str, enum.Enum):
    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


@dataclasses.dataclass
class Offer(
    ObjectBase,
):
    currency_amount: typing.Optional[float] = None
    description: typing.Optional[str] = None
    id: typing.Optional[int] = None
    img: typing.Optional[str] = None
    instruction: typing.Optional[str] = None
    instruction_html: typing.Optional[str] = None
    link_id: typing.Optional[int] = None
    link_type: typing.Optional[str] = None
    price: typing.Optional[int] = None
    short_description: typing.Optional[str] = None
    tag: typing.Optional[str] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class PushConversations(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[PushConversationsItem]] = None


@dataclasses.dataclass
class PushConversationsItem(
    ObjectBase,
):
    disabled_until: int
    peer_id: int
    sound: BoolInt
    disabled_mass_mentions: typing.Optional[BoolInt] = None
    disabled_mentions: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class PushParams(
    ObjectBase,
):
    app_request: typing.Optional[typing.List[PushParamsOnoff]] = None
    birthday: typing.Optional[typing.List[PushParamsOnoff]] = None
    chat: typing.Optional[typing.List[PushParamsMode]] = None
    comment: typing.Optional[typing.List[PushParamsSettings]] = None
    event_soon: typing.Optional[typing.List[PushParamsOnoff]] = None
    friend: typing.Optional[typing.List[PushParamsOnoff]] = None
    friend_accepted: typing.Optional[typing.List[PushParamsOnoff]] = None
    friend_found: typing.Optional[typing.List[PushParamsOnoff]] = None
    group_accepted: typing.Optional[typing.List[PushParamsOnoff]] = None
    group_invite: typing.Optional[typing.List[PushParamsOnoff]] = None
    like: typing.Optional[typing.List[PushParamsSettings]] = None
    mention: typing.Optional[typing.List[PushParamsSettings]] = None
    msg: typing.Optional[typing.List[PushParamsMode]] = None
    new_post: typing.Optional[typing.List[PushParamsOnoff]] = None
    reply: typing.Optional[typing.List[PushParamsOnoff]] = None
    repost: typing.Optional[typing.List[PushParamsSettings]] = None
    sdk_open: typing.Optional[typing.List[PushParamsOnoff]] = None
    wall_post: typing.Optional[typing.List[PushParamsOnoff]] = None
    wall_publish: typing.Optional[typing.List[PushParamsOnoff]] = None


class PushParamsMode(str, enum.Enum):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class PushParamsOnoff(str, enum.Enum):
    ON = "on"
    OFF = "off"


class PushParamsSettings(str, enum.Enum):
    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"


@dataclasses.dataclass
class PushSettings(
    ObjectBase,
):
    conversations: typing.Optional[PushConversations] = None
    disabled: typing.Optional[BoolInt] = None
    disabled_until: typing.Optional[int] = None
    settings: typing.Optional[PushParams] = None


@dataclasses.dataclass
class UserSettings(
    ObjectBase,
    UserMin,
    UserSettingsXtr,
):
    photo_200: typing.Optional[str] = None
    is_service_account: typing.Optional[bool] = None


@dataclasses.dataclass
class UserSettingsInterest(
    ObjectBase,
):
    title: str
    value: str


@dataclasses.dataclass
class UserSettingsInterests(
    ObjectBase,
):
    about: typing.Optional[UserSettingsInterest] = None
    activities: typing.Optional[UserSettingsInterest] = None
    books: typing.Optional[UserSettingsInterest] = None
    games: typing.Optional[UserSettingsInterest] = None
    interests: typing.Optional[UserSettingsInterest] = None
    movies: typing.Optional[UserSettingsInterest] = None
    music: typing.Optional[UserSettingsInterest] = None
    quotes: typing.Optional[UserSettingsInterest] = None
    tv: typing.Optional[UserSettingsInterest] = None
