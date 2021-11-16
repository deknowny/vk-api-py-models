import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Base(
    ObjectBase,
):
    event_id: str
    group_id: int
    type: Type
    secret: typing.Optional[str] = None


@dataclasses.dataclass
class BoardPostDelete(
    ObjectBase,
):
    id: int
    topic_id: int
    topic_owner_id: int


@dataclasses.dataclass
class Confirmation(
    ObjectBase,
    Base,
):
    type: typing.Optional[Type] = "confirmation"


@dataclasses.dataclass
class DonutMoneyWithdraw(
    ObjectBase,
):
    amount: float
    amount_without_fee: float


@dataclasses.dataclass
class DonutMoneyWithdrawError(
    ObjectBase,
):
    reason: str


@dataclasses.dataclass
class DonutSubscriptionCancelled(
    ObjectBase,
):
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class DonutSubscriptionCreate(
    ObjectBase,
):
    amount: int
    amount_without_fee: float
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class DonutSubscriptionExpired(
    ObjectBase,
):
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class DonutSubscriptionPriceChanged(
    ObjectBase,
):
    amount_new: int
    amount_old: int
    amount_diff: typing.Optional[float] = None
    amount_diff_without_fee: typing.Optional[float] = None
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class DonutSubscriptionProlonged(
    ObjectBase,
):
    amount: int
    amount_without_fee: float
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class GroupChangePhoto(
    ObjectBase,
):
    photo: Photo
    user_id: int


@dataclasses.dataclass
class GroupChangeSettings(
    ObjectBase,
):
    self: BoolInt
    user_id: int


@dataclasses.dataclass
class GroupJoin(
    ObjectBase,
):
    join_type: GroupJoinType
    user_id: int


class GroupJoinType(str, enum.Enum):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


@dataclasses.dataclass
class GroupLeave(
    ObjectBase,
):
    self: typing.Optional[BoolInt] = None
    user_id: typing.Optional[int] = None


class GroupMarket(int, enum.Enum):
    DISABLED = 0
    OPEN = 1


class GroupOfficerRole(int, enum.Enum):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


@dataclasses.dataclass
class GroupOfficersEdit(
    ObjectBase,
):
    admin_id: int
    level_new: GroupOfficerRole
    level_old: GroupOfficerRole
    user_id: int


@dataclasses.dataclass
class GroupSettingsChanges(
    ObjectBase,
):
    access: typing.Optional[GroupIsClosed] = None
    age_limits: typing.Optional[GroupFullAgeLimits] = None
    description: typing.Optional[str] = None
    enable_audio: typing.Optional[GroupAudio] = None
    enable_market: typing.Optional[GroupMarket] = None
    enable_photo: typing.Optional[GroupPhotos] = None
    enable_status_default: typing.Optional[GroupWall] = None
    enable_video: typing.Optional[GroupVideo] = None
    public_category: typing.Optional[int] = None
    public_subcategory: typing.Optional[int] = None
    screen_name: typing.Optional[str] = None
    title: typing.Optional[str] = None
    website: typing.Optional[str] = None


@dataclasses.dataclass
class LikeAddRemove(
    ObjectBase,
):
    liker_id: int
    object_id: int
    object_owner_id: int
    object_type: str
    post_id: int
    thread_reply_id: typing.Optional[int] = None


@dataclasses.dataclass
class MarketComment(
    ObjectBase,
):
    date: int
    from_id: int
    id: int
    market_owner_id: typing.Optional[int] = None
    photo_id: typing.Optional[int] = None
    text: typing.Optional[str] = None


@dataclasses.dataclass
class MarketCommentDelete(
    ObjectBase,
):
    id: int
    item_id: int
    owner_id: int
    user_id: int


@dataclasses.dataclass
class MessageAllow(
    ObjectBase,
    Base,
):
    type: typing.Optional[Type] = "message_allow"
    object: typing.Optional[MessageAllowObject] = None


@dataclasses.dataclass
class MessageAllowObject(
    ObjectBase,
):
    key: str
    user_id: int


@dataclasses.dataclass
class MessageDeny(
    ObjectBase,
):
    user_id: int


@dataclasses.dataclass
class MessageEdit(
    ObjectBase,
    Base,
):
    type: typing.Optional[Type] = "message_edit"
    object: typing.Optional[Message] = None


@dataclasses.dataclass
class MessageNew(
    ObjectBase,
    Base,
):
    type: typing.Optional[Type] = "message_new"
    object: typing.Optional[MessageObject] = None


@dataclasses.dataclass
class MessageObject(
    ObjectBase,
):
    client_info: typing.Optional[InfoForBots] = None
    message: typing.Optional[Message] = None


@dataclasses.dataclass
class MessageReply(
    ObjectBase,
    Base,
):
    type: typing.Optional[Type] = "message_reply"
    object: typing.Optional[Message] = None


@dataclasses.dataclass
class PhotoComment(
    ObjectBase,
):
    date: int
    from_id: int
    id: int
    photo_owner_id: int
    text: str


@dataclasses.dataclass
class PhotoCommentDelete(
    ObjectBase,
):
    id: int
    owner_id: int
    photo_id: int
    user_id: int


@dataclasses.dataclass
class PollVoteNew(
    ObjectBase,
):
    option_id: int
    owner_id: int
    poll_id: int
    user_id: int


@dataclasses.dataclass
class QrScan(
    ObjectBase,
):
    data: str
    reread: bool
    subtype: str
    type: str
    user_id: int


class Type(str, enum.Enum):
    AUDIO_NEW = "audio_new"
    BOARD_POST_NEW = "board_post_new"
    BOARD_POST_EDIT = "board_post_edit"
    BOARD_POST_RESTORE = "board_post_restore"
    BOARD_POST_DELETE = "board_post_delete"
    CONFIRMATION = "confirmation"
    GROUP_LEAVE = "group_leave"
    GROUP_JOIN = "group_join"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_NEW = "market_comment_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MESSAGE_NEW = "message_new"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    PHOTO_NEW = "photo_new"
    PHOTO_COMMENT_NEW = "photo_comment_new"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_NEW = "video_new"
    VIDEO_COMMENT_NEW = "video_comment_new"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_POST_NEW = "wall_post_new"
    WALL_REPLY_NEW = "wall_reply_new"
    WALL_REPLY_EDIT = "wall_reply_edit"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"


@dataclasses.dataclass
class UserBlock(
    ObjectBase,
):
    admin_id: int
    reason: int
    unblock_date: int
    user_id: int
    comment: typing.Optional[str] = None


@dataclasses.dataclass
class UserUnblock(
    ObjectBase,
):
    admin_id: int
    by_end_date: int
    user_id: int


@dataclasses.dataclass
class VideoComment(
    ObjectBase,
):
    date: int
    from_id: int
    id: int
    text: str
    video_owner_id: int


@dataclasses.dataclass
class VideoCommentDelete(
    ObjectBase,
):
    id: int
    owner_id: int
    user_id: int
    video_id: int


@dataclasses.dataclass
class WallCommentDelete(
    ObjectBase,
):
    id: int
    owner_id: int
    post_id: int
    user_id: int
