import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class FriendExtendedStatus(
    ObjectBase,
    FriendStatus,
):
    is_request_unread: typing.Optional[bool] = None


@dataclasses.dataclass
class FriendStatus(
    ObjectBase,
):
    friend_status: FriendStatusStatus
    user_id: int
    sign: typing.Optional[str] = None


class FriendStatusStatus(int, enum.Enum):
    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3


@dataclasses.dataclass
class FriendsList(
    ObjectBase,
):
    id: int
    name: str


@dataclasses.dataclass
class MutualFriend(
    ObjectBase,
):
    common_count: typing.Optional[int] = None
    common_friends: typing.Optional[typing.List[int]] = None
    id: typing.Optional[int] = None


@dataclasses.dataclass
class Requests(
    ObjectBase,
):
    field_from: typing.Optional[str] = None
    mutual: typing.Optional[RequestsMutual] = None
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class RequestsMutual(
    ObjectBase,
):
    count: typing.Optional[int] = None
    users: typing.Optional[typing.List[int]] = None


@dataclasses.dataclass
class RequestsXtrMessage(
    ObjectBase,
):
    field_from: typing.Optional[str] = None
    message: typing.Optional[str] = None
    mutual: typing.Optional[RequestsMutual] = None
    user_id: typing.Optional[int] = None


@dataclasses.dataclass
class UserXtrPhone(
    ObjectBase,
    UserFull,
):
    phone: typing.Optional[str] = None
