import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Note(
    ObjectBase,
):
    comments: int
    date: int
    id: int
    owner_id: int
    title: str
    view_url: str
    can_comment: typing.Optional[BoolInt] = None
    privacy_comment: typing.Optional[typing.List[str]] = None
    privacy_view: typing.Optional[typing.List[str]] = None
    read_comments: typing.Optional[int] = None
    text: typing.Optional[str] = None
    text_wiki: typing.Optional[str] = None


@dataclasses.dataclass
class NoteComment(
    ObjectBase,
):
    date: int
    id: int
    message: str
    nid: int
    oid: int
    uid: int
    reply_to: typing.Optional[int] = None
