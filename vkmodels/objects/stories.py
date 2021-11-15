import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class ClickableArea(
    ObjectBase,
):
    x: int
    y: int


@dataclasses.dataclass
class ClickableSticker(
    ObjectBase,
):
    clickable_area: typing.List[ClickableArea]

    id: int
    type: str
    app: typing.Optional[AppMin] = None
    app_context: typing.Optional[str] = None
    audio: typing.Optional[Audio] = None
    audio_start_time: typing.Optional[int] = None
    color: typing.Optional[str] = None
    has_new_interactions: typing.Optional[bool] = None
    hashtag: typing.Optional[str] = None
    is_broadcast_notify_allowed: typing.Optional[bool] = None
    link_object: typing.Optional[Link] = None
    market_item: typing.Optional[MarketItem] = None
    mention: typing.Optional[str] = None
    owner_id: typing.Optional[int] = None
    place_id: typing.Optional[int] = None
    poll: typing.Optional[Poll] = None
    post_id: typing.Optional[int] = None
    post_owner_id: typing.Optional[int] = None
    question: typing.Optional[str] = None
    question_button: typing.Optional[str] = None
    situational_app_url: typing.Optional[str] = None
    situational_theme_id: typing.Optional[int] = None
    sticker_id: typing.Optional[int] = None
    sticker_pack_id: typing.Optional[int] = None
    story_id: typing.Optional[int] = None
    style: typing.Optional[str] = None
    subtype: typing.Optional[str] = None
    tooltip_text: typing.Optional[str] = None


@dataclasses.dataclass
class ClickableStickers(
    ObjectBase,
):
    clickable_stickers: typing.List[ClickableSticker]

    original_height: int
    original_width: int


@dataclasses.dataclass
class FeedItem(
    ObjectBase,
):
    type: str
    app: typing.Optional[AppMin] = None
    birthday_user_id: typing.Optional[int] = None
    grouped: typing.Optional[typing.List[FeedItem]] = None
    has_unseen: typing.Optional[bool] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    promo_data: typing.Optional[PromoBlock] = None
    stories: typing.Optional[typing.List[Story]] = None
    track_code: typing.Optional[str] = None


@dataclasses.dataclass
class PromoBlock(
    ObjectBase,
):
    name: str
    not_animated: bool
    photo_100: str
    photo_50: str


@dataclasses.dataclass
class Replies(
    ObjectBase,
):
    count: int
    new: typing.Optional[int] = None


@dataclasses.dataclass
class StatLine(
    ObjectBase,
):
    name: str
    counter: typing.Optional[int] = None
    is_unavailable: typing.Optional[bool] = None


@dataclasses.dataclass
class Story(
    ObjectBase,
):
    id: int
    owner_id: int
    access_key: typing.Optional[str] = None
    birthday_wish_user_id: typing.Optional[int] = None
    can_ask: typing.Optional[BoolInt] = None
    can_ask_anonymous: typing.Optional[BoolInt] = None
    can_comment: typing.Optional[BoolInt] = None
    can_hide: typing.Optional[BoolInt] = None
    can_like: typing.Optional[bool] = None
    can_reply: typing.Optional[BoolInt] = None
    can_see: typing.Optional[BoolInt] = None
    can_share: typing.Optional[BoolInt] = None
    can_use_in_narrative: typing.Optional[bool] = None
    clickable_stickers: typing.Optional[ClickableStickers] = None
    date: typing.Optional[int] = None
    expires_at: typing.Optional[int] = None
    first_narrative_title: typing.Optional[str] = None
    is_deleted: typing.Optional[bool] = None
    is_expired: typing.Optional[bool] = None
    link: typing.Optional[StoryLink] = None
    narratives_count: typing.Optional[int] = None
    parent_story: typing.Optional[Story] = None
    parent_story_access_key: typing.Optional[str] = None
    parent_story_id: typing.Optional[int] = None
    parent_story_owner_id: typing.Optional[int] = None
    photo: typing.Optional[Photo] = None
    replies: typing.Optional[Replies] = None
    seen: typing.Optional[BoolInt] = None
    type: typing.Optional[StoryType] = None
    video: typing.Optional[Video] = None
    views: typing.Optional[int] = None


@dataclasses.dataclass
class StoryLink(
    ObjectBase,
):
    text: str
    url: str


@dataclasses.dataclass
class StoryStats(
    ObjectBase,
):
    answer: StoryStatsStat
    bans: StoryStatsStat
    likes: StoryStatsStat
    open_link: StoryStatsStat
    replies: StoryStatsStat
    shares: StoryStatsStat
    subscribers: StoryStatsStat
    views: StoryStatsStat


@dataclasses.dataclass
class StoryStatsStat(
    ObjectBase,
):
    state: StoryStatsState
    count: typing.Optional[int] = None


class StoryStatsState(str, enum.Enum):
    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoryType(str, enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    BIRTHDAY_INVITE = "birthday_invite"


class UploadLinkText(str, enum.Enum):
    TO_STORE = "to_store"
    VOTE = "vote"
    MORE = "more"
    BOOK = "book"
    ORDER = "order"
    ENROLL = "enroll"
    FILL = "fill"
    SIGNUP = "signup"
    BUY = "buy"
    TICKET = "ticket"
    WRITE = "write"
    OPEN = "open"
    LEARN_MORE = "learn_more"
    VIEW = "view"
    GO_TO = "go_to"
    CONTACT = "contact"
    WATCH = "watch"
    PLAY = "play"
    INSTALL = "install"
    READ = "read"
    CALENDAR = "calendar"


@dataclasses.dataclass
class ViewersItem(
    ObjectBase,
):
    is_liked: bool
    user_id: int
    user: typing.Optional[UserFull] = None
