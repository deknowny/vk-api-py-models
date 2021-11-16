import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Answer(
    ObjectBase,
):
    id: int
    rate: float
    text: str
    votes: int


@dataclasses.dataclass
class Background(
    ObjectBase,
):
    angle: typing.Optional[int] = None
    color: typing.Optional[str] = None
    height: typing.Optional[int] = None
    id: typing.Optional[int] = None
    images: typing.Optional[typing.List[Image]] = None
    name: typing.Optional[str] = None
    points: typing.Optional[typing.List[GradientPoint]] = None
    type: typing.Optional[str] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class Friend(
    ObjectBase,
):
    id: int


@dataclasses.dataclass
class Poll(
    ObjectBase,
):
    answers: typing.List[Answer]
    can_edit: bool
    can_report: bool
    can_share: bool
    can_vote: bool
    closed: bool
    created: int
    disable_unvote: bool
    end_date: int
    id: int
    is_board: bool
    multiple: bool
    owner_id: int
    question: str
    votes: int
    anonymous: typing.Optional[PollAnonymous] = None
    answer_id: typing.Optional[int] = None
    answer_ids: typing.Optional[typing.List[int]] = None
    author_id: typing.Optional[int] = None
    background: typing.Optional[Background] = None
    embed_hash: typing.Optional[str] = None
    friends: typing.Optional[typing.List[Friend]] = None
    photo: typing.Optional[Background] = None


@dataclasses.dataclass
class Voters(
    ObjectBase,
):
    answer_id: typing.Optional[int] = None
    users: typing.Optional[VotersUsers] = None


@dataclasses.dataclass
class VotersUsers(
    ObjectBase,
):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None
