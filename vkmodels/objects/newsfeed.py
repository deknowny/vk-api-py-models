import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


class CommentsFilters(str, enum.Enum):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class IgnoreItemType(str, enum.Enum):
    POST_ON_THE_WALL = "wall"
    TAG_ON_A_PHOTO = "tag"
    PROFILE_PHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


@dataclasses.dataclass
class ItemAudioAudio(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[Audio]] = None


@dataclasses.dataclass
class ItemBase(
    ObjectBase,
):
    date: int
    source_id: int
    type: NewsfeedItemType


@dataclasses.dataclass
class ItemDigest(
    ObjectBase,
    ItemBase,
):
    feed_id: typing.Optional[str] = None
    items: typing.Optional[typing.List[Wallpost]] = None
    main_post_ids: typing.Optional[typing.List[str]] = None
    template: typing.Optional[str] = None
    header: typing.Optional[ItemDigestHeader] = None
    footer: typing.Optional[ItemDigestFooter] = None
    track_code: typing.Optional[str] = None


@dataclasses.dataclass
class ItemDigestButton(
    ObjectBase,
):
    title: str
    style: typing.Optional[str] = None


@dataclasses.dataclass
class ItemDigestFooter(
    ObjectBase,
):
    style: str
    text: str
    button: typing.Optional[ItemDigestButton] = None


@dataclasses.dataclass
class ItemDigestFullItem(
    ObjectBase,
):
    post: Wallpost
    attachment: typing.Optional[WallpostAttachment] = None
    attachment_index: typing.Optional[int] = None
    source_name: typing.Optional[str] = None
    style: typing.Optional[str] = None
    text: typing.Optional[str] = None


@dataclasses.dataclass
class ItemDigestHeader(
    ObjectBase,
):
    style: str
    title: str
    button: typing.Optional[ItemDigestButton] = None
    subtitle: typing.Optional[str] = None


@dataclasses.dataclass
class ItemDigestItem(
    ObjectBase,
):
    access_key: typing.Optional[str] = None
    is_deleted: typing.Optional[bool] = None
    attachments: typing.Optional[typing.List[WallpostAttachment]] = None
    copyright: typing.Optional[PostCopyright] = None
    date: typing.Optional[int] = None
    edited: typing.Optional[int] = None
    from_id: typing.Optional[int] = None
    geo: typing.Optional[Geo] = None
    id: typing.Optional[int] = None
    is_archived: typing.Optional[bool] = None
    is_favorite: typing.Optional[bool] = None
    likes: typing.Optional[LikesInfo] = None
    owner_id: typing.Optional[int] = None
    post_id: typing.Optional[int] = None
    parents_stack: typing.Optional[typing.List[int]] = None
    post_source: typing.Optional[PostSource] = None
    post_type: typing.Optional[PostType] = None
    reposts: typing.Optional[RepostsInfo] = None
    signer_id: typing.Optional[int] = None
    text: typing.Optional[str] = None
    views: typing.Optional[Views] = None


@dataclasses.dataclass
class ItemFriend(
    ObjectBase,
    ItemBase,
):
    friends: typing.Optional[ItemFriendFriends] = None


@dataclasses.dataclass
class ItemFriendFriends(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[UserId]] = None


@dataclasses.dataclass
class ItemHolidayRecommendationsBlockHeader(
    ObjectBase,
):
    action: typing.Optional[LinkButtonAction] = None
    image: typing.Optional[typing.List[Image]] = None
    subtitle: typing.Optional[str] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class ItemPhotoPhotos(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[NewsfeedPhoto]] = None


@dataclasses.dataclass
class ItemPhotoTagPhotoTags(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[NewsfeedPhoto]] = None


@dataclasses.dataclass
class ItemPromoButton(
    ObjectBase,
    ItemBase,
):
    text: typing.Optional[str] = None
    title: typing.Optional[str] = None
    action: typing.Optional[ItemPromoButtonAction] = None
    images: typing.Optional[typing.List[ItemPromoButtonImage]] = None
    track_code: typing.Optional[str] = None


@dataclasses.dataclass
class ItemPromoButtonAction(
    ObjectBase,
):
    target: typing.Optional[str] = None
    type: typing.Optional[str] = None
    url: typing.Optional[str] = None


@dataclasses.dataclass
class ItemPromoButtonImage(
    ObjectBase,
):
    height: typing.Optional[int] = None
    url: typing.Optional[str] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class ItemTopic(
    ObjectBase,
    ItemBase,
):
    comments: typing.Optional[CommentsInfo] = None
    likes: typing.Optional[LikesInfo] = None
    post_id: typing.Optional[int] = None
    text: typing.Optional[str] = None


@dataclasses.dataclass
class ItemVideoVideo(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[Video]] = None


@dataclasses.dataclass
class ItemWallpostFeedback(
    ObjectBase,
):
    question: str
    type: ItemWallpostFeedbackType
    answers: typing.Optional[typing.List[ItemWallpostFeedbackAnswer]] = None
    gratitude: typing.Optional[str] = None
    stars_count: typing.Optional[int] = None


@dataclasses.dataclass
class ItemWallpostFeedbackAnswer(
    ObjectBase,
):
    id: str
    title: str


class ItemWallpostFeedbackType(str, enum.Enum):
    BUTTONS = "buttons"
    STARS = "stars"


@dataclasses.dataclass
class List(
    ObjectBase,
):
    id: int
    title: str


@dataclasses.dataclass
class ListFull(
    ObjectBase,
    List,
):
    no_reposts: typing.Optional[BoolInt] = None
    source_ids: typing.Optional[typing.List[int]] = None


class NewsfeedItemType(str, enum.Enum):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"
    NOTE = "note"
    AUDIO_PLAYLIST = "audio_playlist"
    CLIP = "clip"


@dataclasses.dataclass
class ItemAudio(
    ObjectBase,
    ItemBase,
):
    audio: typing.Optional[ItemAudioAudio] = None
    post_id: typing.Optional[int] = None


@dataclasses.dataclass
class ItemPhoto(
    ObjectBase,
    CarouselBase,
    ItemBase,
):
    photos: typing.Optional[ItemPhotoPhotos] = None
    post_id: typing.Optional[int] = None


@dataclasses.dataclass
class ItemPhotoTag(
    ObjectBase,
    CarouselBase,
    ItemBase,
):
    photo_tags: typing.Optional[ItemPhotoTagPhotoTags] = None
    post_id: typing.Optional[int] = None


@dataclasses.dataclass
class ItemVideo(
    ObjectBase,
    CarouselBase,
    ItemBase,
):
    video: typing.Optional[ItemVideoVideo] = None


@dataclasses.dataclass
class NewsfeedPhoto(
    ObjectBase,
    Photo,
):
    likes: typing.Optional[Likes] = None
    comments: typing.Optional[ObjectCount] = None
    can_repost: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class ItemWallpost(
    ObjectBase,
    CarouselBase,
    ItemBase,
    WallpostFull,
):
    feedback: typing.Optional[ItemWallpostFeedback] = None


NewsfeedItem: typing.TypeAlias = typing.Union[
    ItemWallpost,
    ItemPhoto,
    ItemPhotoTag,
    ItemFriend,
    ItemAudio,
    ItemVideo,
    ItemTopic,
    ItemDigest,
    ItemPromoButton,
]
