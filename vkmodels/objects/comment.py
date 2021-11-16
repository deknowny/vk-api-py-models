import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Thread(
    ObjectBase,
):
    count: int
    can_post: typing.Optional[bool] = None
    groups_can_post: typing.Optional[bool] = None
    items: typing.Optional[typing.List[WallComment]] = None
    show_reply_button: typing.Optional[bool] = None
