import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


class DefaultOrder(int, enum.Enum):
    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2


@dataclasses.dataclass
class Topic(
    ObjectBase,
):
    comments: typing.Optional[int] = None
    created: typing.Optional[int] = None
    created_by: typing.Optional[int] = None
    id: typing.Optional[int] = None
    is_closed: typing.Optional[BoolInt] = None
    is_fixed: typing.Optional[BoolInt] = None
    title: typing.Optional[str] = None
    updated: typing.Optional[int] = None
    updated_by: typing.Optional[int] = None


@dataclasses.dataclass
class TopicComment(
    ObjectBase,
):
    date: int
    from_id: int
    id: int
    text: str
    attachments: typing.Optional[typing.List[CommentAttachment]] = None
    can_edit: typing.Optional[BoolInt] = None
    likes: typing.Optional[LikesInfo] = None
    real_offset: typing.Optional[int] = None


@dataclasses.dataclass
class TopicPoll(
    ObjectBase,
):
    answer_id: int
    answers: typing.List[Answer]

    created: int
    owner_id: int
    poll_id: int
    question: str
    votes: int
    is_closed: typing.Optional[BoolInt] = None
