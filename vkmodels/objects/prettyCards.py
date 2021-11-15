import dataclasses
import enum
import typing

from vkmodels.bases import ObjectBase


@dataclasses.dataclass
class PrettyCard(
    ObjectBase,
):
    card_id: str
    link_url: str
    photo: str
    title: str
    button: typing.Optional[str] = None
    button_text: typing.Optional[str] = None
    images: typing.Optional[typing.List[Image]] = None
    price: typing.Optional[str] = None
    price_old: typing.Optional[str] = None
