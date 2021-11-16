import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class DonatorSubscriptionInfo(
    ObjectBase,
):
    amount: int
    next_payment_date: int
    owner_id: int
    status: str
