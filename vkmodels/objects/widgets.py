import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class CommentMedia(
    ObjectBase,
):
    item_id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    thumb_src: typing.Optional[str] = None
    type: typing.Optional[CommentMediaType] = None


class CommentMediaType(str, enum.Enum):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


@dataclasses.dataclass
class CommentReplies(
    ObjectBase,
):
    can_post: typing.Optional[BoolInt] = None
    count: typing.Optional[int] = None
    replies: typing.Optional[typing.List[CommentRepliesItem]] = None


@dataclasses.dataclass
class CommentRepliesItem(
    ObjectBase,
):
    cid: typing.Optional[int] = None
    date: typing.Optional[int] = None
    likes: typing.Optional[WidgetLikes] = None
    text: typing.Optional[str] = None
    uid: typing.Optional[int] = None
    user: typing.Optional[UserFull] = None


@dataclasses.dataclass
class WidgetComment(
    ObjectBase,
):
    date: int
    from_id: int
    id: int
    post_type: int
    text: str
    to_id: int
    attachments: typing.Optional[typing.List[CommentAttachment]] = None
    can_delete: typing.Optional[BoolInt] = None
    comments: typing.Optional[CommentReplies] = None
    likes: typing.Optional[LikesInfo] = None
    media: typing.Optional[CommentMedia] = None
    post_source: typing.Optional[PostSource] = None
    reposts: typing.Optional[RepostsInfo] = None
    user: typing.Optional[UserFull] = None


@dataclasses.dataclass
class WidgetLikes(
    ObjectBase,
):
    count: typing.Optional[int] = None


@dataclasses.dataclass
class WidgetPage(
    ObjectBase,
):
    comments: typing.Optional[ObjectCount] = None
    date: typing.Optional[int] = None
    description: typing.Optional[str] = None
    id: typing.Optional[int] = None
    likes: typing.Optional[ObjectCount] = None
    page_id: typing.Optional[str] = None
    photo: typing.Optional[str] = None
    title: typing.Optional[str] = None
    url: typing.Optional[str] = None
