import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class AppPost(
    ObjectBase,
):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    photo_130: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None


@dataclasses.dataclass
class AttachedNote(
    ObjectBase,
):
    comments: int
    date: int
    id: int
    owner_id: int
    read_comments: int
    title: str
    view_url: str
    can_comment: typing.Optional[int] = None
    privacy_comment: typing.Optional[typing.List[str]] = None
    privacy_view: typing.Optional[typing.List[str]] = None
    text: typing.Optional[str] = None
    text_wiki: typing.Optional[str] = None


@dataclasses.dataclass
class CarouselBase(
    ObjectBase,
):
    carousel_offset: typing.Optional[int] = None


@dataclasses.dataclass
class CommentAttachment(
    ObjectBase,
):
    type: CommentAttachmentType
    audio: typing.Optional[Audio] = None
    doc: typing.Optional[Doc] = None
    link: typing.Optional[Link] = None
    market: typing.Optional[MarketItem] = None
    market_market_album: typing.Optional[MarketAlbum] = None
    note: typing.Optional[AttachedNote] = None
    page: typing.Optional[WikipageFull] = None
    photo: typing.Optional[Photo] = None
    sticker: typing.Optional[Sticker] = None
    video: typing.Optional[Video] = None


class CommentAttachmentType(str, enum.Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"


@dataclasses.dataclass
class Geo(
    ObjectBase,
):
    coordinates: typing.Optional[str] = None
    place: typing.Optional[Place] = None
    showmap: typing.Optional[int] = None
    type: typing.Optional[str] = None


class GetFilter(str, enum.Enum):
    OWNER = "owner"
    OTHERS = "others"
    ALL = "all"
    POSTPONED = "postponed"
    SUGGESTS = "suggests"
    ARCHIVED = "archived"
    DONUT = "donut"


@dataclasses.dataclass
class Graffiti(
    ObjectBase,
):
    access_key: typing.Optional[str] = None
    height: typing.Optional[int] = None
    id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    photo_200: typing.Optional[str] = None
    photo_586: typing.Optional[str] = None
    url: typing.Optional[str] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class PostCopyright(
    ObjectBase,
):
    link: str
    name: str
    type: str
    id: typing.Optional[int] = None


@dataclasses.dataclass
class PostSource(
    ObjectBase,
):
    data: typing.Optional[str] = None
    link: typing.Optional[Link] = None
    platform: typing.Optional[str] = None
    type: typing.Optional[PostSourceType] = None
    url: typing.Optional[str] = None


class PostSourceType(str, enum.Enum):
    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    MVK = "mvk"


class PostType(str, enum.Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"
    POST_ADS = "post_ads"
    PHOTO = "photo"
    VIDEO = "video"


@dataclasses.dataclass
class PostedPhoto(
    ObjectBase,
):
    id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    photo_130: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None


@dataclasses.dataclass
class Views(
    ObjectBase,
):
    count: typing.Optional[int] = None


@dataclasses.dataclass
class WallComment(
    ObjectBase,
):
    date: int
    from_id: int
    id: int
    text: str
    attachments: typing.Optional[typing.List[CommentAttachment]] = None
    can_edit: typing.Optional[BoolInt] = None
    deleted: typing.Optional[bool] = None
    donut: typing.Optional[WallCommentDonut] = None
    likes: typing.Optional[LikesInfo] = None
    owner_id: typing.Optional[int] = None
    parents_stack: typing.Optional[typing.List[int]] = None
    photo_id: typing.Optional[int] = None
    pid: typing.Optional[int] = None
    post_id: typing.Optional[int] = None
    real_offset: typing.Optional[int] = None
    reply_to_comment: typing.Optional[int] = None
    reply_to_user: typing.Optional[int] = None
    thread: typing.Optional[Thread] = None
    video_id: typing.Optional[int] = None


@dataclasses.dataclass
class WallCommentDonut(
    ObjectBase,
):
    is_don: typing.Optional[bool] = None
    placeholder: typing.Optional[WallCommentDonutPlaceholder] = None


@dataclasses.dataclass
class WallCommentDonutPlaceholder(
    ObjectBase,
):
    text: str


@dataclasses.dataclass
class Wallpost(
    ObjectBase,
):
    access_key: typing.Optional[str] = None
    attachments: typing.Optional[typing.List[WallpostAttachment]] = None
    copyright: typing.Optional[PostCopyright] = None
    date: typing.Optional[int] = None
    edited: typing.Optional[int] = None
    from_id: typing.Optional[int] = None
    geo: typing.Optional[Geo] = None
    id: typing.Optional[int] = None
    is_archived: typing.Optional[bool] = None
    is_deleted: typing.Optional[bool] = None
    is_favorite: typing.Optional[bool] = None
    likes: typing.Optional[LikesInfo] = None
    owner_id: typing.Optional[int] = None
    parents_stack: typing.Optional[typing.List[int]] = None
    post_id: typing.Optional[int] = None
    post_source: typing.Optional[PostSource] = None
    post_type: typing.Optional[PostType] = None
    reposts: typing.Optional[RepostsInfo] = None
    signer_id: typing.Optional[int] = None
    text: typing.Optional[str] = None
    views: typing.Optional[Views] = None


@dataclasses.dataclass
class WallpostAttachment(
    ObjectBase,
):
    type: WallpostAttachmentType
    access_key: typing.Optional[str] = None
    album: typing.Optional[PhotoAlbum] = None
    app: typing.Optional[AppPost] = None
    audio: typing.Optional[Audio] = None
    doc: typing.Optional[Doc] = None
    event: typing.Optional[EventAttach] = None
    graffiti: typing.Optional[Graffiti] = None
    group: typing.Optional[GroupAttach] = None
    link: typing.Optional[Link] = None
    market: typing.Optional[MarketItem] = None
    market_album: typing.Optional[MarketAlbum] = None
    note: typing.Optional[Note] = None
    page: typing.Optional[WikipageFull] = None
    photo: typing.Optional[Photo] = None
    poll: typing.Optional[Poll] = None
    posted_photo: typing.Optional[PostedPhoto] = None
    video: typing.Optional[VideoFull] = None


class WallpostAttachmentType(str, enum.Enum):
    PHOTO = "photo"
    PHOTOS_LIST = "photos_list"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    AUDIO_PLAYLIST = "audio_playlist"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    MARKET_ALBUM = "market_album"
    MARKET = "market"
    EVENT = "event"
    DONUT_LINK = "donut_link"
    ARTICLE = "article"
    TEXTLIVE = "textlive"
    TEXTPOST = "textpost"
    TEXTPOST_PUBLISH = "textpost_publish"
    SITUATIONAL_THEME = "situational_theme"
    GROUP = "group"
    STICKER = "sticker"
    PODCAST = "podcast"


@dataclasses.dataclass
class WallpostCommentsDonut(
    ObjectBase,
):
    placeholder: typing.Optional[WallpostCommentsDonutPlaceholder] = None


@dataclasses.dataclass
class WallpostCommentsDonutPlaceholder(
    ObjectBase,
):
    text: str


@dataclasses.dataclass
class WallpostDonut(
    ObjectBase,
):
    is_donut: bool
    can_publish_free_copy: typing.Optional[bool] = None
    edit_mode: typing.Optional[str] = None
    paid_duration: typing.Optional[int] = None
    placeholder: typing.Optional[WallpostDonutPlaceholder] = None


@dataclasses.dataclass
class WallpostDonutPlaceholder(
    ObjectBase,
):
    text: str


@dataclasses.dataclass
class WallpostFull(
    ObjectBase,
    CarouselBase,
    Wallpost,
):
    copy_history: typing.Optional[typing.List[WallpostFull]] = None
    can_edit: typing.Optional[BoolInt] = None
    created_by: typing.Optional[int] = None
    can_delete: typing.Optional[BoolInt] = None
    can_pin: typing.Optional[BoolInt] = None
    donut: typing.Optional[WallpostDonut] = None
    is_pinned: typing.Optional[int] = None
    comments: typing.Optional[CommentsInfo] = None
    marked_as_ads: typing.Optional[BoolInt] = None
    topic_id: typing.Optional[int] = None
    short_text_rate: typing.Optional[float] = None
    hash: typing.Optional[str] = None


@dataclasses.dataclass
class WallpostToId(
    ObjectBase,
):
    attachments: typing.Optional[typing.List[WallpostAttachment]] = None
    comments: typing.Optional[CommentsInfo] = None
    copy_owner_id: typing.Optional[int] = None
    copy_post_id: typing.Optional[int] = None
    date: typing.Optional[int] = None
    from_id: typing.Optional[int] = None
    geo: typing.Optional[Geo] = None
    id: typing.Optional[int] = None
    is_favorite: typing.Optional[bool] = None
    likes: typing.Optional[LikesInfo] = None
    post_id: typing.Optional[int] = None
    post_source: typing.Optional[PostSource] = None
    post_type: typing.Optional[PostType] = None
    reposts: typing.Optional[RepostsInfo] = None
    signer_id: typing.Optional[int] = None
    text: typing.Optional[str] = None
    to_id: typing.Optional[int] = None
