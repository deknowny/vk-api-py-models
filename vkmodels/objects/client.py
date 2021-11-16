import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class InfoForBots(
    ObjectBase,
):
    button_actions: typing.Optional[
        typing.List[TemplateActionTypeNames]
    ] = None
    carousel: typing.Optional[bool] = None
    inline_keyboard: typing.Optional[bool] = None
    keyboard: typing.Optional[bool] = None
    lang_id: typing.Optional[int] = None
