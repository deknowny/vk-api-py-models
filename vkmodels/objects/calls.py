import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Call(
    ObjectBase,
):
    initiator_id: int
    receiver_id: int
    state: EndState
    time: int
    duration: typing.Optional[int] = None
    participants: typing.Optional[Participants] = None
    video: typing.Optional[bool] = None


class EndState(str, enum.Enum):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"


@dataclasses.dataclass
class Participants(
    ObjectBase,
):
    count: typing.Optional[int] = None
    list: typing.Optional[typing.List[int]] = None
