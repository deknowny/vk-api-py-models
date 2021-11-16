import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Feedback(
    ObjectBase,
):
    attachments: typing.Optional[typing.List[WallpostAttachment]] = None
    from_id: typing.Optional[int] = None
    geo: typing.Optional[Geo] = None
    id: typing.Optional[int] = None
    likes: typing.Optional[LikesInfo] = None
    text: typing.Optional[str] = None
    to_id: typing.Optional[int] = None


@dataclasses.dataclass
class Notification(
    ObjectBase,
):
    date: typing.Optional[int] = None
    feedback: typing.Optional[Feedback] = None
    parent: typing.Optional[Notification] = None
    reply: typing.Optional[Reply] = None
    type: typing.Optional[str] = None


@dataclasses.dataclass
class NotificationItem(
    ObjectBase,
):
    date: typing.Optional[int] = None
    feedback: typing.Optional[Feedback] = None
    parent: typing.Optional[Notification] = None
    reply: typing.Optional[Reply] = None
    type: typing.Optional[str] = None


@dataclasses.dataclass
class NotificationsComment(
    ObjectBase,
):
    date: typing.Optional[int] = None
    id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    photo: typing.Optional[Photo] = None
    post: typing.Optional[Wallpost] = None
    text: typing.Optional[str] = None
    topic: typing.Optional[Topic] = None
    video: typing.Optional[Video] = None


@dataclasses.dataclass
class Reply(
    ObjectBase,
):
    date: typing.Optional[int] = None
    id: typing.Optional[int] = None
    text: typing.Optional[int] = None


@dataclasses.dataclass
class SendMessageError(
    ObjectBase,
):
    code: typing.Optional[int] = None
    description: typing.Optional[str] = None


@dataclasses.dataclass
class SendMessageItem(
    ObjectBase,
):
    error: typing.Optional[SendMessageError] = None
    status: typing.Optional[bool] = None
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class NotificationParent(
    ObjectBase,
    WallpostToId,
    Photo,
    Topic,
    Video,
    NotificationsComment,
):
    pass
