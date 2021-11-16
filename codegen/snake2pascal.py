import re
import typing


def _upper_zero_group(match: typing.Match) -> str:
    return match.group("let").upper()


def snake2pascal(name: str) -> str:
    return re.sub(r"(?:_|\A)(?P<let>[a-z])", _upper_zero_group, name)
