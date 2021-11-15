import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class Amount(
    ObjectBase,
):
    amounts: typing.Optional[typing.List[AmountItem]] = None
    currency: typing.Optional[str] = None


@dataclasses.dataclass
class AmountItem(
    ObjectBase,
):
    amount: typing.Optional[float] = None
    description: typing.Optional[str] = None
    votes: typing.Optional[str] = None


@dataclasses.dataclass
class Order(
    ObjectBase,
):
    amount: str
    app_order_id: str
    date: str
    id: str
    item: str
    receiver_id: str
    status: str
    user_id: str
    cancel_transaction_id: typing.Optional[str] = None
    transaction_id: typing.Optional[str] = None


@dataclasses.dataclass
class Subscription(
    ObjectBase,
):
    create_time: int
    id: int
    item_id: str
    period: int
    period_start_time: int
    price: int
    status: str
    update_time: int
    app_id: typing.Optional[int] = None
    application_name: typing.Optional[str] = None
    cancel_reason: typing.Optional[str] = None
    expire_time: typing.Optional[int] = None
    next_bill_time: typing.Optional[int] = None
    pending_cancel: typing.Optional[bool] = None
    photo_url: typing.Optional[str] = None
    test_mode: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    trial_expire_time: typing.Optional[int] = None
