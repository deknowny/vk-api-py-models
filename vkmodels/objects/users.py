import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Career(
    ObjectBase,
):
    city_id: typing.Optional[int] = None
    city_name: typing.Optional[str] = None
    company: typing.Optional[str] = None
    country_id: typing.Optional[int] = None
    field_from: typing.Optional[int] = None
    group_id: typing.Optional[int] = None
    id: typing.Optional[int] = None
    position: typing.Optional[str] = None
    until: typing.Optional[int] = None


@dataclasses.dataclass
class Exports(
    ObjectBase,
):
    facebook: typing.Optional[int] = None
    livejournal: typing.Optional[int] = None
    twitter: typing.Optional[int] = None


class Fields(str, enum.Enum):
    FIRST_NAME_NOM = "first_name_nom"
    FIRST_NAME_GEN = "first_name_gen"
    FIRST_NAME_DAT = "first_name_dat"
    FIRST_NAME_ACC = "first_name_acc"
    FIRST_NAME_INS = "first_name_ins"
    FIRST_NAME_ABL = "first_name_abl"
    LAST_NAME_NOM = "last_name_nom"
    LAST_NAME_GEN = "last_name_gen"
    LAST_NAME_DAT = "last_name_dat"
    LAST_NAME_ACC = "last_name_acc"
    LAST_NAME_INS = "last_name_ins"
    LAST_NAME_ABL = "last_name_abl"
    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    CITY = "city"
    COUNTRY = "country"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO = "photo"
    PHOTO_REC = "photo_rec"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400 = "photo_400"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_BIG = "photo_big"
    PHOTO_MEDIUM = "photo_medium"
    PHOTO_MEDIUM_REC = "photo_medium_rec"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    PHOTO_MAX_SIZE = "photo_max_size"
    THIRD_PARTY_BUTTONS = "third_party_buttons"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    LANGUAGE = "language"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    ONLINE_INFO = "online_info"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    WALL_DEFAULT = "wall_default"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    IS_NO_INDEX = "is_no_index"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEE_GIFTS = "can_see_gifts"
    WORK = "work"
    PLACES = "places"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_DOC = "can_upload_doc"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
    FRIEND_STATUS = "friend_status"
    CAREER = "career"
    MILITARY = "military"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    DESCRIPTIONS = "descriptions"
    TRENDING = "trending"
    MUTUAL = "mutual"
    FRIENDSHIP_WEEKS = "friendship_weeks"
    CAN_INVITE_TO_CHATS = "can_invite_to_chats"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    VIDEO_LIVE = "video_live"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    SERVICE_DESCRIPTION = "service_description"
    CAN_SEE_WISHES = "can_see_wishes"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"


@dataclasses.dataclass
class LastSeen(
    ObjectBase,
):
    platform: typing.Optional[int] = None
    time: typing.Optional[int] = None


@dataclasses.dataclass
class Military(
    ObjectBase,
):
    country_id: int
    unit: str
    unit_id: int
    field_from: typing.Optional[int] = None
    id: typing.Optional[int] = None
    until: typing.Optional[int] = None


@dataclasses.dataclass
class Occupation(
    ObjectBase,
):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    type: typing.Optional[str] = None


@dataclasses.dataclass
class OnlineInfo(
    ObjectBase,
):
    visible: bool
    app_id: typing.Optional[int] = None
    is_mobile: typing.Optional[bool] = None
    is_online: typing.Optional[bool] = None
    last_seen: typing.Optional[int] = None
    status: typing.Optional[str] = None


@dataclasses.dataclass
class Personal(
    ObjectBase,
):
    alcohol: typing.Optional[int] = None
    inspired_by: typing.Optional[str] = None
    langs: typing.Optional[typing.List[str]] = None
    life_main: typing.Optional[int] = None
    people_main: typing.Optional[int] = None
    political: typing.Optional[int] = None
    religion: typing.Optional[str] = None
    religion_id: typing.Optional[int] = None
    smoking: typing.Optional[int] = None


@dataclasses.dataclass
class Relative(
    ObjectBase,
):
    type: str
    birth_date: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None


@dataclasses.dataclass
class School(
    ObjectBase,
):
    city: typing.Optional[int] = None
    field_class: typing.Optional[str] = None
    country: typing.Optional[int] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    speciality: typing.Optional[str] = None
    type: typing.Optional[int] = None
    type_str: typing.Optional[str] = None
    year_from: typing.Optional[int] = None
    year_graduated: typing.Optional[int] = None
    year_to: typing.Optional[int] = None


SubscriptionsItem: typing.TypeAlias = typing.Union[
    UserXtrType,
    GroupFull,
]


@dataclasses.dataclass
class University(
    ObjectBase,
):
    chair: typing.Optional[int] = None
    chair_name: typing.Optional[str] = None
    city: typing.Optional[int] = None
    country: typing.Optional[int] = None
    education_form: typing.Optional[str] = None
    education_status: typing.Optional[str] = None
    faculty: typing.Optional[int] = None
    faculty_name: typing.Optional[str] = None
    graduation: typing.Optional[int] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    university_group_id: typing.Optional[int] = None


@dataclasses.dataclass
class User(
    ObjectBase,
    UserMin,
):
    sex: typing.Optional[Sex] = None
    screen_name: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    photo_100: typing.Optional[str] = None
    online_info: typing.Optional[OnlineInfo] = None
    online: typing.Optional[BoolInt] = None
    online_mobile: typing.Optional[BoolInt] = None
    online_app: typing.Optional[int] = None
    verified: typing.Optional[BoolInt] = None
    trending: typing.Optional[BoolInt] = None
    friend_status: typing.Optional[FriendStatusStatus] = None
    mutual: typing.Optional[RequestsMutual] = None


@dataclasses.dataclass
class UserConnections(
    ObjectBase,
):
    facebook: str
    instagram: str
    skype: str
    twitter: str
    facebook_name: typing.Optional[str] = None
    livejournal: typing.Optional[str] = None


@dataclasses.dataclass
class UserCounters(
    ObjectBase,
):
    albums: typing.Optional[int] = None
    articles: typing.Optional[int] = None
    audios: typing.Optional[int] = None
    badges: typing.Optional[int] = None
    clips: typing.Optional[int] = None
    clips_followers: typing.Optional[int] = None
    followers: typing.Optional[int] = None
    friends: typing.Optional[int] = None
    gifts: typing.Optional[int] = None
    groups: typing.Optional[int] = None
    mutual_friends: typing.Optional[int] = None
    new_photo_tags: typing.Optional[int] = None
    new_recognition_tags: typing.Optional[int] = None
    notes: typing.Optional[int] = None
    online_friends: typing.Optional[int] = None
    pages: typing.Optional[int] = None
    photos: typing.Optional[int] = None
    podcasts: typing.Optional[int] = None
    posts: typing.Optional[int] = None
    subscriptions: typing.Optional[int] = None
    user_photos: typing.Optional[int] = None
    user_videos: typing.Optional[int] = None
    videos: typing.Optional[int] = None
    wishes: typing.Optional[int] = None


@dataclasses.dataclass
class UserFull(
    ObjectBase,
    User,
):
    first_name_nom: typing.Optional[str] = None
    first_name_gen: typing.Optional[str] = None
    first_name_dat: typing.Optional[str] = None
    first_name_acc: typing.Optional[str] = None
    first_name_ins: typing.Optional[str] = None
    first_name_abl: typing.Optional[str] = None
    last_name_nom: typing.Optional[str] = None
    last_name_gen: typing.Optional[str] = None
    last_name_dat: typing.Optional[str] = None
    last_name_acc: typing.Optional[str] = None
    last_name_ins: typing.Optional[str] = None
    last_name_abl: typing.Optional[str] = None
    nickname: typing.Optional[str] = None
    maiden_name: typing.Optional[str] = None
    contact_name: typing.Optional[str] = None
    domain: typing.Optional[str] = None
    bdate: typing.Optional[str] = None
    city: typing.Optional[City] = None
    country: typing.Optional[Country] = None
    timezone: typing.Optional[float] = None
    owner_state: typing.Optional[State] = None
    photo_200: typing.Optional[str] = None
    photo_max: typing.Optional[str] = None
    photo_200_orig: typing.Optional[str] = None
    photo_400_orig: typing.Optional[str] = None
    photo_max_orig: typing.Optional[str] = None
    photo_id: typing.Optional[str] = None
    has_photo: typing.Optional[BoolInt] = None
    has_mobile: typing.Optional[BoolInt] = None
    is_friend: typing.Optional[BoolInt] = None
    wall_comments: typing.Optional[BoolInt] = None
    can_post: typing.Optional[BoolInt] = None
    can_see_all_posts: typing.Optional[BoolInt] = None
    can_see_audio: typing.Optional[BoolInt] = None
    type: typing.Optional[UserType] = None
    email: typing.Optional[str] = None
    skype: typing.Optional[str] = None
    facebook: typing.Optional[str] = None
    facebook_name: typing.Optional[str] = None
    twitter: typing.Optional[str] = None
    livejournal: typing.Optional[str] = None
    instagram: typing.Optional[str] = None
    test: typing.Optional[BoolInt] = None
    video_live: typing.Optional[LiveInfo] = None
    is_video_live_notifications_blocked: typing.Optional[BoolInt] = None
    is_service: typing.Optional[bool] = None
    service_description: typing.Optional[str] = None
    photo_rec: typing.Optional[PhotoFalseable] = None
    photo_medium: typing.Optional[PhotoFalseable] = None
    photo_medium_rec: typing.Optional[PhotoFalseable] = None
    photo: typing.Optional[str] = None
    photo_big: typing.Optional[str] = None
    photo_400: typing.Optional[str] = None
    photo_max_size: typing.Optional[Photo] = None
    language: typing.Optional[str] = None
    stories_archive_count: typing.Optional[int] = None
    has_unseen_stories: typing.Optional[bool] = None
    wall_default: typing.Optional[str] = None
    can_call: typing.Optional[bool] = None
    can_call_from_group: typing.Optional[bool] = None
    can_see_wishes: typing.Optional[bool] = None
    can_see_gifts: typing.Optional[BoolInt] = None
    interests: typing.Optional[str] = None
    books: typing.Optional[str] = None
    tv: typing.Optional[str] = None
    quotes: typing.Optional[str] = None
    about: typing.Optional[str] = None
    games: typing.Optional[str] = None
    movies: typing.Optional[str] = None
    activities: typing.Optional[str] = None
    music: typing.Optional[str] = None
    can_write_private_message: typing.Optional[BoolInt] = None
    can_send_friend_request: typing.Optional[BoolInt] = None
    can_be_invited_group: typing.Optional[bool] = None
    mobile_phone: typing.Optional[str] = None
    home_phone: typing.Optional[str] = None
    site: typing.Optional[str] = None
    status_audio: typing.Optional[Audio] = None
    status: typing.Optional[str] = None
    activity: typing.Optional[str] = None
    last_seen: typing.Optional[LastSeen] = None
    exports: typing.Optional[Exports] = None
    crop_photo: typing.Optional[CropPhoto] = None
    followers_count: typing.Optional[int] = None
    video_live_level: typing.Optional[int] = None
    video_live_count: typing.Optional[int] = None
    clips_count: typing.Optional[int] = None
    blacklisted: typing.Optional[BoolInt] = None
    blacklisted_by_me: typing.Optional[BoolInt] = None
    is_favorite: typing.Optional[BoolInt] = None
    is_hidden_from_feed: typing.Optional[BoolInt] = None
    common_count: typing.Optional[int] = None
    occupation: typing.Optional[Occupation] = None
    career: typing.Optional[typing.List[Career]] = None
    military: typing.Optional[typing.List[Military]] = None
    university: typing.Optional[int] = None
    university_name: typing.Optional[str] = None
    university_group_id: typing.Optional[int] = None
    faculty: typing.Optional[int] = None
    faculty_name: typing.Optional[str] = None
    graduation: typing.Optional[int] = None
    education_form: typing.Optional[str] = None
    education_status: typing.Optional[str] = None
    home_town: typing.Optional[str] = None
    relation: typing.Optional[UserRelation] = None
    relation_partner: typing.Optional[UserMin] = None
    personal: typing.Optional[Personal] = None
    universities: typing.Optional[typing.List[University]] = None
    schools: typing.Optional[typing.List[School]] = None
    relatives: typing.Optional[typing.List[Relative]] = None
    is_subscribed_podcasts: typing.Optional[bool] = None
    can_subscribe_podcasts: typing.Optional[bool] = None
    can_subscribe_posts: typing.Optional[bool] = None
    counters: typing.Optional[UserCounters] = None
    access_key: typing.Optional[str] = None
    can_upload_doc: typing.Optional[BoolInt] = None
    hash: typing.Optional[str] = None
    is_no_index: typing.Optional[bool] = None
    contact_id: typing.Optional[int] = None
    is_message_request: typing.Optional[bool] = None
    descriptions: typing.Optional[typing.List[str]] = None
    lists: typing.Optional[typing.List[int]] = None


@dataclasses.dataclass
class UserMin(
    ObjectBase,
):
    first_name: str
    id: int
    last_name: str
    can_access_closed: typing.Optional[bool] = None
    deactivated: typing.Optional[str] = None
    hidden: typing.Optional[int] = None
    is_closed: typing.Optional[bool] = None


class UserRelation(int, enum.Enum):
    NOT_SPECIFIED = 0
    SINGLE = 1
    IN_A_RELATIONSHIP = 2
    ENGAGED = 3
    MARRIED = 4
    COMPLICATED = 5
    ACTIVELY_SEARCHING = 6
    IN_LOVE = 7
    IN_A_CIVIL_UNION = 8


@dataclasses.dataclass
class UserSettingsXtr(
    ObjectBase,
):
    home_town: str
    status: str
    bdate: typing.Optional[str] = None
    bdate_visibility: typing.Optional[int] = None
    city: typing.Optional[City] = None
    connections: typing.Optional[UserConnections] = None
    country: typing.Optional[Country] = None
    first_name: typing.Optional[str] = None
    interests: typing.Optional[UserSettingsInterests] = None
    languages: typing.Optional[typing.List[str]] = None
    last_name: typing.Optional[str] = None
    maiden_name: typing.Optional[str] = None
    name_request: typing.Optional[NameRequest] = None
    personal: typing.Optional[Personal] = None
    phone: typing.Optional[str] = None
    relation: typing.Optional[UserRelation] = None
    relation_partner: typing.Optional[UserMin] = None
    relation_pending: typing.Optional[BoolInt] = None
    relation_requests: typing.Optional[typing.List[UserMin]] = None
    screen_name: typing.Optional[str] = None
    sex: typing.Optional[Sex] = None
    status_audio: typing.Optional[Audio] = None


class UserType(str, enum.Enum):
    PROFILE = "profile"


@dataclasses.dataclass
class UserXtrType(
    ObjectBase,
    User,
):
    type: typing.Optional[UserType] = None


@dataclasses.dataclass
class UsersArray(
    ObjectBase,
):
    count: int
    items: typing.List[int]
