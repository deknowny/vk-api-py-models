import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Address(
    ObjectBase,
):
    id: int
    additional_address: typing.Optional[str] = None
    address: typing.Optional[str] = None
    city_id: typing.Optional[int] = None
    country_id: typing.Optional[int] = None
    distance: typing.Optional[int] = None
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    metro_station_id: typing.Optional[int] = None
    phone: typing.Optional[str] = None
    place_id: typing.Optional[int] = None
    time_offset: typing.Optional[int] = None
    timetable: typing.Optional[AddressTimetable] = None
    title: typing.Optional[str] = None
    work_info_status: typing.Optional[AddressWorkInfoStatus] = None


@dataclasses.dataclass
class AddressTimetable(
    ObjectBase,
):
    fri: typing.Optional[AddressTimetableDay] = None
    mon: typing.Optional[AddressTimetableDay] = None
    sat: typing.Optional[AddressTimetableDay] = None
    sun: typing.Optional[AddressTimetableDay] = None
    thu: typing.Optional[AddressTimetableDay] = None
    tue: typing.Optional[AddressTimetableDay] = None
    wed: typing.Optional[AddressTimetableDay] = None


@dataclasses.dataclass
class AddressTimetableDay(
    ObjectBase,
):
    close_time: int
    open_time: int
    break_close_time: typing.Optional[int] = None
    break_open_time: typing.Optional[int] = None


class AddressWorkInfoStatus(str, enum.Enum):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


@dataclasses.dataclass
class AddressesInfo(
    ObjectBase,
):
    is_enabled: bool
    main_address_id: typing.Optional[int] = None


@dataclasses.dataclass
class BanInfo(
    ObjectBase,
):
    admin_id: typing.Optional[int] = None
    comment: typing.Optional[str] = None
    comment_visible: typing.Optional[bool] = None
    date: typing.Optional[int] = None
    end_date: typing.Optional[int] = None
    is_closed: typing.Optional[bool] = None
    reason: typing.Optional[BanInfoReason] = None


class BanInfoReason(int, enum.Enum):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4


@dataclasses.dataclass
class BannedItem(
    ObjectBase,
):
    ban_info: typing.Optional[BanInfo] = None
    group: typing.Optional[Group] = None
    profile: typing.Optional[User] = None
    type: typing.Optional[OwnerXtrBanInfoType] = None


@dataclasses.dataclass
class CallbackServer(
    ObjectBase,
):
    creator_id: int
    id: int
    secret_key: str
    status: str
    title: str
    url: str


@dataclasses.dataclass
class CallbackSettings(
    ObjectBase,
):
    api_version: typing.Optional[str] = None
    events: typing.Optional[LongPollEvents] = None


@dataclasses.dataclass
class ContactsItem(
    ObjectBase,
):
    desc: typing.Optional[str] = None
    email: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class CountersGroup(
    ObjectBase,
):
    addresses: typing.Optional[int] = None
    albums: typing.Optional[int] = None
    articles: typing.Optional[int] = None
    audio_playlists: typing.Optional[int] = None
    audios: typing.Optional[int] = None
    clips: typing.Optional[int] = None
    clips_followers: typing.Optional[int] = None
    docs: typing.Optional[int] = None
    market: typing.Optional[int] = None
    market_services: typing.Optional[int] = None
    narratives: typing.Optional[int] = None
    photos: typing.Optional[int] = None
    podcasts: typing.Optional[int] = None
    topics: typing.Optional[int] = None
    videos: typing.Optional[int] = None


@dataclasses.dataclass
class Cover(
    ObjectBase,
):
    enabled: BoolInt
    images: typing.Optional[typing.List[Image]] = None


class Fields(str, enum.Enum):
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
    CITY = "city"
    COUNTRY = "country"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    REQUESTS_COUNT = "requests_count"
    COUNTERS = "counters"
    COVER = "cover"
    CAN_POST = "can_post"
    CAN_SUGGEST = "can_suggest"
    CAN_UPLOAD_STORY = "can_upload_story"
    CAN_UPLOAD_DOC = "can_upload_doc"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_UPLOAD_CLIP = "can_upload_clip"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_CREATE_TOPIC = "can_create_topic"
    CROP_PHOTO = "crop_photo"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    HAS_PHOTO = "has_photo"
    STATUS = "status"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    SITE = "site"
    MAIN_SECTION = "main_section"
    SECONDARY_SECTION = "secondary_section"
    WALL = "wall"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    HAS_GROUP_CHANNEL = "has_group_channel"
    GROUP_CHANNEL = "group_channel"
    ONLINE_STATUS = "online_status"
    START_DATE = "start_date"
    FINISH_DATE = "finish_date"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    ACTION_BUTTON = "action_button"
    AUTHOR_ID = "author_id"
    PHONE = "phone"
    HAS_MARKET_APP = "has_market_app"
    ADDRESSES = "addresses"
    LIVE_COVERS = "live_covers"
    IS_ADULT = "is_adult"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    WARNING_NOTIFICATION = "warning_notification"
    MSG_PUSH_ALLOWED = "msg_push_allowed"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    IS_BUSINESS = "is_business"
    TEXTLIVES_COUNT = "textlives_count"


class Filter(str, enum.Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


@dataclasses.dataclass
class Group(
    ObjectBase,
):
    id: int
    is_closed: GroupIsClosed
    name: str
    screen_name: str
    admin_level: typing.Optional[GroupAdminLevel] = None
    deactivated: typing.Optional[str] = None
    est_date: typing.Optional[str] = None
    finish_date: typing.Optional[int] = None
    is_admin: typing.Optional[BoolInt] = None
    is_advertiser: typing.Optional[BoolInt] = None
    is_member: typing.Optional[BoolInt] = None
    is_video_live_notifications_blocked: typing.Optional[BoolInt] = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_200_orig: typing.Optional[str] = None
    photo_400: typing.Optional[str] = None
    photo_400_orig: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    photo_max: typing.Optional[str] = None
    photo_max_orig: typing.Optional[str] = None
    photo_max_size: typing.Optional[PhotoSize] = None
    public_date_label: typing.Optional[str] = None
    start_date: typing.Optional[int] = None
    type: typing.Optional[GroupType] = None
    video_live: typing.Optional[LiveInfo] = None


class GroupAccess(int, enum.Enum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupAdminLevel(int, enum.Enum):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupAgeLimits(int, enum.Enum):
    UNLIMITED = 1
    FIELD_16_PLUS = 2
    FIELD_18_PLUS = 3


@dataclasses.dataclass
class GroupAttach(
    ObjectBase,
):
    id: int
    is_favorite: bool
    size: int
    status: str
    text: str


class GroupAudio(int, enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


@dataclasses.dataclass
class GroupBanInfo(
    ObjectBase,
):
    comment: typing.Optional[str] = None
    end_date: typing.Optional[int] = None
    reason: typing.Optional[BanInfoReason] = None


@dataclasses.dataclass
class GroupCategory(
    ObjectBase,
):
    id: int
    name: str
    subcategories: typing.Optional[typing.List[ObjectWithName]] = None


@dataclasses.dataclass
class GroupCategoryFull(
    ObjectBase,
):
    id: int
    name: str
    page_count: int
    page_previews: typing.List[Group]
    subcategories: typing.Optional[typing.List[GroupCategory]] = None


@dataclasses.dataclass
class GroupCategoryType(
    ObjectBase,
):
    id: int
    name: str


class GroupDocs(int, enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


@dataclasses.dataclass
class GroupFull(
    ObjectBase,
    Group,
):
    market: typing.Optional[MarketInfo] = None
    member_status: typing.Optional[GroupFullMemberStatus] = None
    is_adult: typing.Optional[BoolInt] = None
    is_hidden_from_feed: typing.Optional[BoolInt] = None
    is_favorite: typing.Optional[BoolInt] = None
    is_subscribed: typing.Optional[BoolInt] = None
    city: typing.Optional[Object] = None
    country: typing.Optional[Country] = None
    verified: typing.Optional[BoolInt] = None
    description: typing.Optional[str] = None
    wiki_page: typing.Optional[str] = None
    members_count: typing.Optional[int] = None
    requests_count: typing.Optional[int] = None
    video_live_level: typing.Optional[int] = None
    video_live_count: typing.Optional[int] = None
    clips_count: typing.Optional[int] = None
    counters: typing.Optional[CountersGroup] = None
    cover: typing.Optional[Cover] = None
    can_post: typing.Optional[BoolInt] = None
    can_suggest: typing.Optional[BoolInt] = None
    can_upload_story: typing.Optional[BoolInt] = None
    can_upload_doc: typing.Optional[BoolInt] = None
    can_upload_video: typing.Optional[BoolInt] = None
    can_see_all_posts: typing.Optional[BoolInt] = None
    can_create_topic: typing.Optional[BoolInt] = None
    activity: typing.Optional[str] = None
    fixed_post: typing.Optional[int] = None
    has_photo: typing.Optional[BoolInt] = None
    crop_photo: typing.Optional[CropPhoto] = None
    status: typing.Optional[str] = None
    status_audio: typing.Optional[Audio] = None
    main_album_id: typing.Optional[int] = None
    links: typing.Optional[typing.List[LinksItem]] = None
    contacts: typing.Optional[typing.List[ContactsItem]] = None
    wall: typing.Optional[int] = None
    site: typing.Optional[str] = None
    main_section: typing.Optional[GroupFullSection] = None
    secondary_section: typing.Optional[GroupFullSection] = None
    trending: typing.Optional[BoolInt] = None
    can_message: typing.Optional[BoolInt] = None
    is_messages_blocked: typing.Optional[BoolInt] = None
    can_send_notify: typing.Optional[BoolInt] = None
    online_status: typing.Optional[OnlineStatus] = None
    invited_by: typing.Optional[int] = None
    age_limits: typing.Optional[GroupFullAgeLimits] = None
    ban_info: typing.Optional[GroupBanInfo] = None
    has_market_app: typing.Optional[bool] = None
    using_vkpay_market_app: typing.Optional[bool] = None
    has_group_channel: typing.Optional[bool] = None
    addresses: typing.Optional[AddressesInfo] = None
    is_subscribed_podcasts: typing.Optional[bool] = None
    can_subscribe_podcasts: typing.Optional[bool] = None
    is_subscribed_stories: typing.Optional[bool] = None
    can_subscribe_stories: typing.Optional[bool] = None
    can_subscribe_posts: typing.Optional[bool] = None
    live_covers: typing.Optional[LiveCovers] = None
    stories_archive_count: typing.Optional[int] = None
    has_unseen_stories: typing.Optional[bool] = None


class GroupFullAgeLimits(int, enum.Enum):
    NO = 1
    OVER_16 = 2
    OVER_18 = 3


class GroupFullMemberStatus(int, enum.Enum):
    NOT_A_MEMBER = 0
    MEMBER = 1
    NOT_SURE = 2
    DECLINED = 3
    HAS_SENT_A_REQUEST = 4
    INVITED = 5


class GroupFullSection(int, enum.Enum):
    ABSENT = 0
    PHOTOS = 1
    TOPICS = 2
    AUDIO = 3
    VIDEO = 4
    MARKET = 5
    EVENTS = 10
    ADDRESSES = 35
    ARTICLES = 39
    CHATS = 43
    MARKET_SERVICES = 51


class GroupIsClosed(int, enum.Enum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupMarketCurrency(int, enum.Enum):
    RUSSIAN_RUBLES = 643
    UKRAINIAN_HRYVNIA = 980
    KAZAKH_TENGE = 398
    EURO = 978
    US_DOLLARS = 840


class GroupPhotos(int, enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


@dataclasses.dataclass
class GroupPublicCategoryList(
    ObjectBase,
):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    subcategories: typing.Optional[typing.List[GroupCategoryType]] = None


class GroupRole(str, enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupSubject(str, enum.Enum):
    AUTO = "1"
    ACTIVITY_HOLIDAYS = "2"
    BUSINESS = "3"
    PETS = "4"
    HEALTH = "5"
    DATING_AND_COMMUNICATION = "6"
    GAMES = "7"
    IT = "8"
    CINEMA = "9"
    BEAUTY_AND_FASHION = "10"
    COOKING = "11"
    ART_AND_CULTURE = "12"
    LITERATURE = "13"
    MOBILE_SERVICES_AND_INTERNET = "14"
    MUSIC = "15"
    SCIENCE_AND_TECHNOLOGY = "16"
    REAL_ESTATE = "17"
    NEWS_AND_MEDIA = "18"
    SECURITY = "19"
    EDUCATION = "20"
    HOME_AND_RENOVATIONS = "21"
    POLITICS = "22"
    FOOD = "23"
    INDUSTRY = "24"
    TRAVEL = "25"
    WORK = "26"
    ENTERTAINMENT = "27"
    RELIGION = "28"
    FAMILY = "29"
    SPORTS = "30"
    INSURANCE = "31"
    TELEVISION = "32"
    GOODS_AND_SERVICES = "33"
    HOBBIES = "34"
    FINANCE = "35"
    PHOTO = "36"
    ESOTERICS = "37"
    ELECTRONICS_AND_APPLIANCES = "38"
    EROTIC = "39"
    HUMOR = "40"
    SOCIETY_HUMANITIES = "41"
    DESIGN_AND_GRAPHICS = "42"


class GroupSuggestedPrivacy(int, enum.Enum):
    NONE = 0
    ALL = 1
    SUBSCRIBERS = 2


@dataclasses.dataclass
class GroupTag(
    ObjectBase,
):
    color: str
    id: int
    name: str
    uses: typing.Optional[int] = None


class GroupTopics(int, enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupType(str, enum.Enum):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupVideo(int, enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupWall(int, enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CLOSED = 3


class GroupWiki(int, enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


@dataclasses.dataclass
class GroupsArray(
    ObjectBase,
):
    count: int
    items: typing.List[int]


@dataclasses.dataclass
class LinksItem(
    ObjectBase,
):
    desc: typing.Optional[str] = None
    edit_title: typing.Optional[BoolInt] = None
    id: typing.Optional[int] = None
    image_processing: typing.Optional[BoolInt] = None
    name: typing.Optional[str] = None
    photo_100: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    url: typing.Optional[str] = None


@dataclasses.dataclass
class LiveCovers(
    ObjectBase,
):
    is_enabled: bool
    is_scalable: typing.Optional[bool] = None
    story_ids: typing.Optional[typing.List[str]] = None


@dataclasses.dataclass
class LongPollEvents(
    ObjectBase,
):
    audio_new: BoolInt
    board_post_delete: BoolInt
    board_post_edit: BoolInt
    board_post_new: BoolInt
    board_post_restore: BoolInt
    donut_money_withdraw: BoolInt
    donut_money_withdraw_error: BoolInt
    donut_subscription_cancelled: BoolInt
    donut_subscription_create: BoolInt
    donut_subscription_expired: BoolInt
    donut_subscription_price_changed: BoolInt
    donut_subscription_prolonged: BoolInt
    group_change_photo: BoolInt
    group_change_settings: BoolInt
    group_join: BoolInt
    group_leave: BoolInt
    group_officers_edit: BoolInt
    market_comment_delete: BoolInt
    market_comment_edit: BoolInt
    market_comment_new: BoolInt
    market_comment_restore: BoolInt
    message_allow: BoolInt
    message_deny: BoolInt
    message_edit: BoolInt
    message_new: BoolInt
    message_read: BoolInt
    message_reply: BoolInt
    message_typing_state: BoolInt
    photo_comment_delete: BoolInt
    photo_comment_edit: BoolInt
    photo_comment_new: BoolInt
    photo_comment_restore: BoolInt
    photo_new: BoolInt
    poll_vote_new: BoolInt
    user_block: BoolInt
    user_unblock: BoolInt
    video_comment_delete: BoolInt
    video_comment_edit: BoolInt
    video_comment_new: BoolInt
    video_comment_restore: BoolInt
    video_new: BoolInt
    wall_post_new: BoolInt
    wall_reply_delete: BoolInt
    wall_reply_edit: BoolInt
    wall_reply_new: BoolInt
    wall_reply_restore: BoolInt
    wall_repost: BoolInt
    lead_forms_new: typing.Optional[BoolInt] = None
    market_order_edit: typing.Optional[BoolInt] = None
    market_order_new: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class LongPollServer(
    ObjectBase,
):
    key: str
    server: str
    ts: str


@dataclasses.dataclass
class LongPollSettings(
    ObjectBase,
):
    events: LongPollEvents
    is_enabled: bool
    api_version: typing.Optional[str] = None


@dataclasses.dataclass
class MarketInfo(
    ObjectBase,
):
    contact_id: typing.Optional[int] = None
    currency: typing.Optional[Currency] = None
    currency_text: typing.Optional[str] = None
    enabled: typing.Optional[BoolInt] = None
    main_album_id: typing.Optional[int] = None
    min_order_price: typing.Optional[Price] = None
    price_max: typing.Optional[str] = None
    price_min: typing.Optional[str] = None
    type: typing.Optional[str] = None


class MarketState(str, enum.Enum):
    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"


@dataclasses.dataclass
class MemberRole(
    ObjectBase,
):
    id: int
    permissions: typing.Optional[typing.List[MemberRolePermission]] = None
    role: typing.Optional[MemberRoleStatus] = None


class MemberRolePermission(str, enum.Enum):
    ADS = "ads"


class MemberRoleStatus(str, enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    ADVERTISER = "advertiser"


@dataclasses.dataclass
class MemberStatus(
    ObjectBase,
):
    member: BoolInt
    user_id: int


@dataclasses.dataclass
class MemberStatusFull(
    ObjectBase,
):
    member: BoolInt
    user_id: int
    can_invite: typing.Optional[BoolInt] = None
    can_recall: typing.Optional[BoolInt] = None
    invitation: typing.Optional[BoolInt] = None
    request: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class OnlineStatus(
    ObjectBase,
):
    status: OnlineStatusType
    minutes: typing.Optional[int] = None


class OnlineStatusType(str, enum.Enum):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


@dataclasses.dataclass
class OwnerXtrBanInfo(
    ObjectBase,
):
    ban_info: typing.Optional[BanInfo] = None
    group: typing.Optional[Group] = None
    profile: typing.Optional[User] = None
    type: typing.Optional[OwnerXtrBanInfoType] = None


class OwnerXtrBanInfoType(str, enum.Enum):
    GROUP = "group"
    PROFILE = "profile"


@dataclasses.dataclass
class PhotoSize(
    ObjectBase,
):
    height: int
    width: int


class RoleOptions(str, enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


@dataclasses.dataclass
class SettingsTwitter(
    ObjectBase,
):
    status: str
    name: typing.Optional[str] = None


@dataclasses.dataclass
class SubjectItem(
    ObjectBase,
):
    id: int
    name: str


@dataclasses.dataclass
class TokenPermissionSetting(
    ObjectBase,
):
    name: str
    setting: int


@dataclasses.dataclass
class UserXtrRole(
    ObjectBase,
    UserFull,
):
    role: typing.Optional[RoleOptions] = None
