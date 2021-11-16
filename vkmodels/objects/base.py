import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


class BoolInt(int, enum.Enum):
    NO = 0
    YES = 1


@dataclasses.dataclass
class City(
    ObjectBase,
):
    id: int
    title: str


@dataclasses.dataclass
class CommentsInfo(
    ObjectBase,
):
    can_close: typing.Optional[BoolInt] = None
    can_open: typing.Optional[BoolInt] = None
    can_post: typing.Optional[BoolInt] = None
    count: typing.Optional[int] = None
    donut: typing.Optional[WallpostCommentsDonut] = None
    groups_can_post: typing.Optional[bool] = None


@dataclasses.dataclass
class Country(
    ObjectBase,
):
    id: int
    title: str


@dataclasses.dataclass
class CropPhoto(
    ObjectBase,
):
    crop: CropPhotoCrop
    photo: Photo
    rect: CropPhotoRect


@dataclasses.dataclass
class CropPhotoCrop(
    ObjectBase,
):
    x: float
    x2: float
    y: float
    y2: float


@dataclasses.dataclass
class CropPhotoRect(
    ObjectBase,
):
    x: float
    x2: float
    y: float
    y2: float


@dataclasses.dataclass
class Error(
    ObjectBase,
):
    error_code: int
    error_msg: typing.Optional[str] = None
    error_subcode: typing.Optional[int] = None
    error_text: typing.Optional[str] = None
    request_params: typing.Optional[typing.List[RequestParam]] = None


@dataclasses.dataclass
class Geo(
    ObjectBase,
):
    coordinates: typing.Optional[GeoCoordinates] = None
    place: typing.Optional[Place] = None
    showmap: typing.Optional[int] = None
    type: typing.Optional[str] = None


@dataclasses.dataclass
class GeoCoordinates(
    ObjectBase,
):
    latitude: float
    longitude: float


@dataclasses.dataclass
class GradientPoint(
    ObjectBase,
):
    color: str
    position: float


@dataclasses.dataclass
class Image(
    ObjectBase,
):
    height: int
    url: str
    width: int
    id: typing.Optional[str] = None


@dataclasses.dataclass
class Likes(
    ObjectBase,
):
    count: typing.Optional[int] = None
    user_likes: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class LikesInfo(
    ObjectBase,
):
    can_like: BoolInt
    count: int
    user_likes: int
    can_publish: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class Link(
    ObjectBase,
):
    url: str
    application: typing.Optional[LinkApplication] = None
    button: typing.Optional[LinkButton] = None
    caption: typing.Optional[str] = None
    description: typing.Optional[str] = None
    id: typing.Optional[str] = None
    is_external: typing.Optional[bool] = None
    is_favorite: typing.Optional[bool] = None
    photo: typing.Optional[Photo] = None
    preview_page: typing.Optional[str] = None
    preview_url: typing.Optional[str] = None
    product: typing.Optional[LinkProduct] = None
    rating: typing.Optional[LinkRating] = None
    target_object: typing.Optional[TargetObject] = None
    title: typing.Optional[str] = None
    video: typing.Optional[Video] = None


@dataclasses.dataclass
class LinkApplication(
    ObjectBase,
):
    app_id: typing.Optional[float] = None
    store: typing.Optional[LinkApplicationStore] = None


@dataclasses.dataclass
class LinkApplicationStore(
    ObjectBase,
):
    id: typing.Optional[float] = None
    name: typing.Optional[str] = None


@dataclasses.dataclass
class LinkButton(
    ObjectBase,
):
    action: typing.Optional[LinkButtonAction] = None
    album_id: typing.Optional[int] = None
    block_id: typing.Optional[str] = None
    curator_id: typing.Optional[int] = None
    icon: typing.Optional[str] = None
    owner_id: typing.Optional[int] = None
    section_id: typing.Optional[str] = None
    style: typing.Optional[LinkButtonStyle] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class LinkButtonAction(
    ObjectBase,
):
    type: LinkButtonActionType
    consume_reason: typing.Optional[str] = None
    url: typing.Optional[str] = None


class LinkButtonActionType(str, enum.Enum):
    OPEN_URL = "open_url"


class LinkButtonStyle(str, enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


@dataclasses.dataclass
class LinkProduct(
    ObjectBase,
):
    price: Price
    merchant: typing.Optional[str] = None
    orders_count: typing.Optional[int] = None


class LinkProductStatus(str, enum.Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"


@dataclasses.dataclass
class LinkRating(
    ObjectBase,
):
    reviews_count: typing.Optional[int] = None
    stars: typing.Optional[float] = None


@dataclasses.dataclass
class MessageError(
    ObjectBase,
):
    code: typing.Optional[int] = None
    description: typing.Optional[str] = None


@dataclasses.dataclass
class Object(
    ObjectBase,
):
    id: int
    title: str


@dataclasses.dataclass
class ObjectCount(
    ObjectBase,
):
    count: typing.Optional[int] = None


@dataclasses.dataclass
class ObjectWithName(
    ObjectBase,
):
    id: int
    name: str


@dataclasses.dataclass
class Place(
    ObjectBase,
):
    address: typing.Optional[str] = None
    checkins: typing.Optional[int] = None
    city: typing.Optional[str] = None
    country: typing.Optional[str] = None
    created: typing.Optional[int] = None
    icon: typing.Optional[str] = None
    id: typing.Optional[int] = None
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    title: typing.Optional[str] = None
    type: typing.Optional[str] = None


class PropertyExists(int, enum.Enum):
    PROPERTY_EXISTS = 1


@dataclasses.dataclass
class RepostsInfo(
    ObjectBase,
):
    count: int
    mail_count: typing.Optional[int] = None
    user_reposted: typing.Optional[int] = None
    wall_count: typing.Optional[int] = None


@dataclasses.dataclass
class RequestParam(
    ObjectBase,
):
    key: typing.Optional[str] = None
    value: typing.Optional[str] = None


class Sex(int, enum.Enum):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2


@dataclasses.dataclass
class StickerAnimation(
    ObjectBase,
):
    type: typing.Optional[str] = None
    url: typing.Optional[str] = None


@dataclasses.dataclass
class StickerNew(
    ObjectBase,
):
    animation_url: typing.Optional[str] = None
    animations: typing.Optional[typing.List[StickerAnimation]] = None
    images: typing.Optional[typing.List[Image]] = None
    images_with_background: typing.Optional[typing.List[Image]] = None
    is_allowed: typing.Optional[bool] = None
    product_id: typing.Optional[int] = None
    sticker_id: typing.Optional[int] = None


@dataclasses.dataclass
class StickerOld(
    ObjectBase,
):
    height: typing.Optional[int] = None
    id: typing.Optional[int] = None
    is_allowed: typing.Optional[bool] = None
    photo_128: typing.Optional[str] = None
    photo_256: typing.Optional[str] = None
    photo_352: typing.Optional[str] = None
    photo_512: typing.Optional[str] = None
    photo_64: typing.Optional[str] = None
    product_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class UploadServer(
    ObjectBase,
):
    upload_url: str


class UserGroupFields(str, enum.Enum):
    ABOUT = "about"
    ACTION_BUTTON = "action_button"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    ADDRESSES = "addresses"
    ADMIN_LEVEL = "admin_level"
    AGE_LIMITS = "age_limits"
    AUTHOR_ID = "author_id"
    BAN_INFO = "ban_info"
    BDATE = "bdate"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    BOOKS = "books"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_MESSAGE = "can_message"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAREER = "career"
    CITY = "city"
    COMMON_COUNT = "common_count"
    CONNECTIONS = "connections"
    CONTACTS = "contacts"
    COUNTERS = "counters"
    COUNTRY = "country"
    COVER = "cover"
    CROP_PHOTO = "crop_photo"
    DEACTIVATED = "deactivated"
    DESCRIPTION = "description"
    DOMAIN = "domain"
    EDUCATION = "education"
    EXPORTS = "exports"
    FINISH_DATE = "finish_date"
    FIXED_POST = "fixed_post"
    FOLLOWERS_COUNT = "followers_count"
    FRIEND_STATUS = "friend_status"
    GAMES = "games"
    HAS_MARKET_APP = "has_market_app"
    HAS_MOBILE = "has_mobile"
    HAS_PHOTO = "has_photo"
    HOME_TOWN = "home_town"
    ID = "id"
    INTERESTS = "interests"
    IS_ADMIN = "is_admin"
    IS_CLOSED = "is_closed"
    IS_FAVORITE = "is_favorite"
    IS_FRIEND = "is_friend"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_MEMBER = "is_member"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    IS_SUBSCRIBED = "is_subscribed"
    LAST_SEEN = "last_seen"
    LINKS = "links"
    LISTS = "lists"
    MAIDEN_NAME = "maiden_name"
    MAIN_ALBUM_ID = "main_album_id"
    MAIN_SECTION = "main_section"
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    MEMBERS_COUNT = "members_count"
    MILITARY = "military"
    MOVIES = "movies"
    MUSIC = "music"
    NAME = "name"
    NICKNAME = "nickname"
    OCCUPATION = "occupation"
    ONLINE = "online"
    ONLINE_STATUS = "online_status"
    PERSONAL = "personal"
    PHONE = "phone"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_50 = "photo_50"
    PHOTO_ID = "photo_id"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    QUOTES = "quotes"
    RELATION = "relation"
    RELATIVES = "relatives"
    SCHOOLS = "schools"
    SCREEN_NAME = "screen_name"
    SEX = "sex"
    SITE = "site"
    START_DATE = "start_date"
    STATUS = "status"
    TIMEZONE = "timezone"
    TRENDING = "trending"
    TV = "tv"
    TYPE = "type"
    UNIVERSITIES = "universities"
    VERIFIED = "verified"
    WALL_COMMENTS = "wall_comments"
    WIKI_PAGE = "wiki_page"
    VK_ADMIN_STATUS = "vk_admin_status"


@dataclasses.dataclass
class UserId(
    ObjectBase,
):
    user_id: typing.Optional[int] = None


Sticker: typing.TypeAlias = typing.Union[
    StickerOld,
    StickerNew,
]
