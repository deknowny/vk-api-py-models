import abc
import dataclasses


@dataclasses.dataclass
class ObjectBase(abc.ABC):
    mapping: dict

