import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class TargetObject(
    ObjectBase,
):
    item_id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    type: typing.Optional[str] = None
