import typing
import re


def _upper_zero_group(match: typing.Match, /) -> str:
    return match.group("let").upper()


def snake2camel(name: str, /) -> str:
    return re.sub(r"_(?P<let>[a-z])", _upper_zero_group, name).title()
