import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class AudioMessage(
    ObjectBase,
):
    duration: int
    id: int
    link_mp3: str
    link_ogg: str
    owner_id: int
    waveform: typing.List[int]
    access_key: typing.Optional[str] = None
    transcript_error: typing.Optional[int] = None


@dataclasses.dataclass
class Chat(
    ObjectBase,
):
    admin_id: int
    id: int
    type: str
    users: typing.List[int]
    is_default_photo: typing.Optional[bool] = None
    kicked: typing.Optional[BoolInt] = None
    left: typing.Optional[BoolInt] = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    push_settings: typing.Optional[ChatPushSettings] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class ChatFull(
    ObjectBase,
):
    admin_id: int
    id: int
    type: str
    users: typing.List[UserXtrInvitedBy]
    kicked: typing.Optional[BoolInt] = None
    left: typing.Optional[BoolInt] = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    push_settings: typing.Optional[ChatPushSettings] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class ChatPreview(
    ObjectBase,
):
    admin_id: typing.Optional[int] = None
    is_member: typing.Optional[bool] = None
    joined: typing.Optional[bool] = None
    local_id: typing.Optional[int] = None
    members: typing.Optional[typing.List[int]] = None
    members_count: typing.Optional[int] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class ChatPushSettings(
    ObjectBase,
):
    disabled_until: typing.Optional[int] = None
    sound: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class ChatRestrictions(
    ObjectBase,
):
    admins_promote_users: typing.Optional[bool] = None
    only_admins_edit_info: typing.Optional[bool] = None
    only_admins_edit_pin: typing.Optional[bool] = None
    only_admins_invite: typing.Optional[bool] = None
    only_admins_kick: typing.Optional[bool] = None


@dataclasses.dataclass
class ChatSettings(
    ObjectBase,
):
    acl: ChatSettingsAcl
    active_ids: typing.List[int]
    owner_id: int
    state: ChatSettingsState
    title: str
    admin_ids: typing.Optional[typing.List[int]] = None
    disappearing_chat_link: typing.Optional[str] = None
    friends_count: typing.Optional[int] = None
    is_disappearing: typing.Optional[bool] = None
    is_group_channel: typing.Optional[bool] = None
    is_service: typing.Optional[bool] = None
    members_count: typing.Optional[int] = None
    permissions: typing.Optional[ChatSettingsPermissions] = None
    photo: typing.Optional[ChatSettingsPhoto] = None
    pinned_message: typing.Optional[PinnedMessage] = None
    theme: typing.Optional[str] = None


@dataclasses.dataclass
class ChatSettingsAcl(
    ObjectBase,
):
    can_call: bool
    can_change_info: bool
    can_change_invite_link: bool
    can_change_pin: bool
    can_copy_chat: bool
    can_invite: bool
    can_moderate: bool
    can_promote_users: bool
    can_see_invite_link: bool
    can_use_mass_mentions: bool
    can_change_service_type: typing.Optional[bool] = None


@dataclasses.dataclass
class ChatSettingsPermissions(
    ObjectBase,
):
    call: typing.Optional[str] = None
    change_admins: typing.Optional[str] = None
    change_info: typing.Optional[str] = None
    change_pin: typing.Optional[str] = None
    invite: typing.Optional[str] = None
    see_invite_link: typing.Optional[str] = None
    use_mass_mentions: typing.Optional[str] = None


@dataclasses.dataclass
class ChatSettingsPhoto(
    ObjectBase,
):
    is_default_call_photo: typing.Optional[bool] = None
    is_default_photo: typing.Optional[bool] = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None


class ChatSettingsState(str, enum.Enum):
    FIELD_IN = "in"
    KICKED = "kicked"
    LEFT = "left"


@dataclasses.dataclass
class Conversation(
    ObjectBase,
):
    in_read: int
    last_message_id: int
    out_read: int
    peer: ConversationPeer
    can_write: typing.Optional[ConversationCanWrite] = None
    chat_settings: typing.Optional[ChatSettings] = None
    current_keyboard: typing.Optional[Keyboard] = None
    important: typing.Optional[bool] = None
    is_marked_unread: typing.Optional[bool] = None
    last_conversation_message_id: typing.Optional[int] = None
    mentions: typing.Optional[typing.List[int]] = None
    message_request_data: typing.Optional[MessageRequestData] = None
    out_read_by: typing.Optional[OutReadBy] = None
    push_settings: typing.Optional[PushSettings] = None
    sort_id: typing.Optional[ConversationSortId] = None
    special_service_type: typing.Optional[str] = None
    unanswered: typing.Optional[bool] = None
    unread_count: typing.Optional[int] = None


@dataclasses.dataclass
class ConversationCanWrite(
    ObjectBase,
):
    allowed: bool
    reason: typing.Optional[int] = None


@dataclasses.dataclass
class ConversationMember(
    ObjectBase,
):
    member_id: int
    can_kick: typing.Optional[bool] = None
    invited_by: typing.Optional[int] = None
    is_admin: typing.Optional[bool] = None
    is_message_request: typing.Optional[bool] = None
    is_owner: typing.Optional[bool] = None
    join_date: typing.Optional[int] = None
    request_date: typing.Optional[int] = None


@dataclasses.dataclass
class ConversationPeer(
    ObjectBase,
):
    id: int
    type: ConversationPeerType
    local_id: typing.Optional[int] = None


class ConversationPeerType(str, enum.Enum):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


@dataclasses.dataclass
class ConversationSortId(
    ObjectBase,
):
    major_id: int
    minor_id: int


@dataclasses.dataclass
class ConversationWithMessage(
    ObjectBase,
):
    conversation: Conversation
    last_message: typing.Optional[Message] = None


@dataclasses.dataclass
class ForeignMessage(
    ObjectBase,
):
    date: int
    from_id: int
    text: str
    attachments: typing.Optional[typing.List[MessageAttachment]] = None
    conversation_message_id: typing.Optional[int] = None
    fwd_messages: typing.Optional[typing.List[ForeignMessage]] = None
    geo: typing.Optional[Geo] = None
    id: typing.Optional[int] = None
    payload: typing.Optional[str] = None
    peer_id: typing.Optional[int] = None
    reply_message: typing.Optional[ForeignMessage] = None
    update_time: typing.Optional[int] = None
    was_listened: typing.Optional[bool] = None


@dataclasses.dataclass
class Forward(
    ObjectBase,
):
    conversation_message_ids: typing.Optional[typing.List[int]] = None
    is_reply: typing.Optional[bool] = None
    message_ids: typing.Optional[typing.List[int]] = None
    owner_id: typing.Optional[int] = None
    peer_id: typing.Optional[int] = None


@dataclasses.dataclass
class GetConversationById(
    ObjectBase,
):
    count: int
    items: typing.List[Conversation]


@dataclasses.dataclass
class GetConversationByIdExtended(
    ObjectBase,
    GetConversationById,
):
    profiles: typing.Optional[typing.List[UserFull]] = None
    groups: typing.Optional[typing.List[GroupFull]] = None


@dataclasses.dataclass
class GetConversationMembers(
    ObjectBase,
):
    count: int
    items: typing.List[ConversationMember]
    chat_restrictions: typing.Optional[ChatRestrictions] = None
    groups: typing.Optional[typing.List[GroupFull]] = None
    profiles: typing.Optional[typing.List[UserFull]] = None


@dataclasses.dataclass
class Graffiti(
    ObjectBase,
):
    height: int
    id: int
    owner_id: int
    url: str
    width: int
    access_key: typing.Optional[str] = None


@dataclasses.dataclass
class HistoryAttachment(
    ObjectBase,
):
    attachment: HistoryMessageAttachment
    from_id: int
    message_id: int
    forward_level: typing.Optional[int] = None


@dataclasses.dataclass
class HistoryMessageAttachment(
    ObjectBase,
):
    type: HistoryMessageAttachmentType
    audio: typing.Optional[Audio] = None
    audio_message: typing.Optional[AudioMessage] = None
    doc: typing.Optional[Doc] = None
    graffiti: typing.Optional[Graffiti] = None
    link: typing.Optional[Link] = None
    market: typing.Optional[Link] = None
    photo: typing.Optional[Photo] = None
    share: typing.Optional[Link] = None
    video: typing.Optional[Video] = None
    wall: typing.Optional[Link] = None


class HistoryMessageAttachmentType(str, enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    WALL = "wall"
    SHARE = "share"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


@dataclasses.dataclass
class Keyboard(
    ObjectBase,
):
    buttons: typing.List[typing.List[KeyboardButton]]
    one_time: bool
    author_id: typing.Optional[int] = None
    inline: typing.Optional[bool] = None


@dataclasses.dataclass
class KeyboardButton(
    ObjectBase,
):
    action: KeyboardButtonAction
    color: typing.Optional[str] = None


@dataclasses.dataclass
class KeyboardButtonAction(
    ObjectBase,
):
    type: TemplateActionTypeNames
    app_id: typing.Optional[int] = None
    hash: typing.Optional[str] = None
    label: typing.Optional[str] = None
    link: typing.Optional[str] = None
    owner_id: typing.Optional[int] = None
    payload: typing.Optional[str] = None


@dataclasses.dataclass
class LastActivity(
    ObjectBase,
):
    online: BoolInt
    time: int


@dataclasses.dataclass
class LongpollMessages(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[Message]] = None


@dataclasses.dataclass
class LongpollParams(
    ObjectBase,
):
    key: str
    server: str
    ts: int
    pts: typing.Optional[int] = None


@dataclasses.dataclass
class Message(
    ObjectBase,
):
    date: int
    from_id: int
    id: int
    out: BoolInt
    peer_id: int
    text: str
    action: typing.Optional[MessageAction] = None
    admin_author_id: typing.Optional[int] = None
    attachments: typing.Optional[typing.List[MessageAttachment]] = None
    conversation_message_id: typing.Optional[int] = None
    deleted: typing.Optional[BoolInt] = None
    fwd_messages: typing.Optional[typing.List[ForeignMessage]] = None
    geo: typing.Optional[Geo] = None
    important: typing.Optional[bool] = None
    is_cropped: typing.Optional[bool] = None
    is_hidden: typing.Optional[bool] = None
    is_silent: typing.Optional[bool] = None
    keyboard: typing.Optional[Keyboard] = None
    members_count: typing.Optional[int] = None
    payload: typing.Optional[str] = None
    pinned_at: typing.Optional[int] = None
    random_id: typing.Optional[int] = None
    ref: typing.Optional[str] = None
    ref_source: typing.Optional[str] = None
    reply_message: typing.Optional[ForeignMessage] = None
    update_time: typing.Optional[int] = None
    was_listened: typing.Optional[bool] = None


@dataclasses.dataclass
class MessageAction(
    ObjectBase,
):
    type: MessageActionStatus
    conversation_message_id: typing.Optional[int] = None
    email: typing.Optional[str] = None
    member_id: typing.Optional[int] = None
    message: typing.Optional[str] = None
    photo: typing.Optional[MessageActionPhoto] = None
    text: typing.Optional[str] = None


@dataclasses.dataclass
class MessageActionPhoto(
    ObjectBase,
):
    photo_100: str
    photo_200: str
    photo_50: str


class MessageActionStatus(str, enum.Enum):
    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"
    CHAT_INVITE_USER_BY_MESSAGE_REQUEST = (
        "chat_invite_user_by_message_request"
    )
    CHAT_SCREENSHOT = "chat_screenshot"


@dataclasses.dataclass
class MessageAttachment(
    ObjectBase,
):
    type: MessageAttachmentType
    audio: typing.Optional[Audio] = None
    audio_message: typing.Optional[AudioMessage] = None
    call: typing.Optional[Call] = None
    doc: typing.Optional[Doc] = None
    gift: typing.Optional[Layout] = None
    graffiti: typing.Optional[Graffiti] = None
    link: typing.Optional[Link] = None
    market: typing.Optional[MarketItem] = None
    market_market_album: typing.Optional[MarketAlbum] = None
    photo: typing.Optional[Photo] = None
    poll: typing.Optional[Poll] = None
    sticker: typing.Optional[Sticker] = None
    story: typing.Optional[Story] = None
    video: typing.Optional[Video] = None
    wall: typing.Optional[WallpostFull] = None
    wall_reply: typing.Optional[WallComment] = None


class MessageAttachmentType(str, enum.Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    POLL = "poll"
    CALL = "call"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


@dataclasses.dataclass
class MessageRequestData(
    ObjectBase,
):
    inviter_id: typing.Optional[int] = None
    request_date: typing.Optional[int] = None
    status: typing.Optional[str] = None


@dataclasses.dataclass
class MessagesArray(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[Message]] = None


@dataclasses.dataclass
class OutReadBy(
    ObjectBase,
):
    count: typing.Optional[int] = None
    member_ids: typing.Optional[typing.List[int]] = None


@dataclasses.dataclass
class PinnedMessage(
    ObjectBase,
):
    date: int
    from_id: int
    id: int
    peer_id: int
    text: str
    attachments: typing.Optional[typing.List[MessageAttachment]] = None
    conversation_message_id: typing.Optional[int] = None
    fwd_messages: typing.Optional[typing.List[ForeignMessage]] = None
    geo: typing.Optional[Geo] = None
    keyboard: typing.Optional[Keyboard] = None
    reply_message: typing.Optional[ForeignMessage] = None


@dataclasses.dataclass
class PushSettings(
    ObjectBase,
):
    disabled_forever: bool
    no_sound: bool
    disabled_mass_mentions: typing.Optional[bool] = None
    disabled_mentions: typing.Optional[bool] = None
    disabled_until: typing.Optional[int] = None


@dataclasses.dataclass
class SendUserIdsResponseItem(
    ObjectBase,
):
    message_id: int
    peer_id: int
    conversation_message_id: typing.Optional[int] = None
    error: typing.Optional[MessageError] = None


class TemplateActionTypeNames(str, enum.Enum):
    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"
    CALLBACK = "callback"
    INTENT_SUBSCRIBE = "intent_subscribe"
    INTENT_UNSUBSCRIBE = "intent_unsubscribe"


@dataclasses.dataclass
class UserXtrInvitedBy(
    ObjectBase,
    UserXtrType,
):
    invited_by: typing.Optional[int] = None
