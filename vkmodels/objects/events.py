import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class EventAttach(
    ObjectBase,
):
    button_text: str
    friends: typing.List[int]

    id: int
    is_favorite: bool
    text: str
    address: typing.Optional[str] = None
    member_status: typing.Optional[GroupFullMemberStatus] = None
    time: typing.Optional[int] = None
