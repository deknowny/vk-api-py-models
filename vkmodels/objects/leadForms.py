import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Answer(
    ObjectBase,
):
    answer: typing.Union[
        AnswerItem,
        typing.List[AnswerItem],
    ]
    key: str


@dataclasses.dataclass
class AnswerItem(
    ObjectBase,
):
    value: str
    key: typing.Optional[str] = None


@dataclasses.dataclass
class Form(
    ObjectBase,
):
    form_id: int
    group_id: int
    leads_count: int
    url: str
    active: typing.Optional[BoolInt] = None
    confirmation: typing.Optional[str] = None
    description: typing.Optional[str] = None
    name: typing.Optional[str] = None
    notify_admins: typing.Optional[str] = None
    notify_emails: typing.Optional[str] = None
    once_per_user: typing.Optional[int] = None
    photo: typing.Optional[str] = None
    pixel_code: typing.Optional[str] = None
    policy_link_url: typing.Optional[str] = None
    questions: typing.Optional[typing.List[QuestionItem]] = None
    site_link_url: typing.Optional[str] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class Lead(
    ObjectBase,
):
    answers: typing.List[Answer]
    date: int
    lead_id: int
    user_id: int
    ad_id: typing.Optional[int] = None


@dataclasses.dataclass
class QuestionItem(
    ObjectBase,
):
    key: str
    type: str
    label: typing.Optional[str] = None
    options: typing.Optional[typing.List[QuestionItemOption]] = None


@dataclasses.dataclass
class QuestionItemOption(
    ObjectBase,
):
    label: str
    key: typing.Optional[str] = None
