import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Doc(
    ObjectBase,
):
    date: int
    ext: str
    id: int
    owner_id: int
    size: int
    title: str
    type: int
    access_key: typing.Optional[str] = None
    is_licensed: typing.Optional[BoolInt] = None
    preview: typing.Optional[DocPreview] = None
    tags: typing.Optional[typing.List[str]] = None
    url: typing.Optional[str] = None


class DocAttachmentType(str, enum.Enum):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


@dataclasses.dataclass
class DocPreview(
    ObjectBase,
):
    audio_msg: typing.Optional[DocPreviewAudioMsg] = None
    graffiti: typing.Optional[DocPreviewGraffiti] = None
    photo: typing.Optional[DocPreviewPhoto] = None
    video: typing.Optional[DocPreviewVideo] = None


@dataclasses.dataclass
class DocPreviewAudioMsg(
    ObjectBase,
):
    duration: int
    link_mp3: str
    link_ogg: str
    waveform: typing.List[int]


@dataclasses.dataclass
class DocPreviewGraffiti(
    ObjectBase,
):
    height: int
    src: str
    width: int


@dataclasses.dataclass
class DocPreviewPhoto(
    ObjectBase,
):
    sizes: typing.Optional[typing.List[DocPreviewPhotoSizes]] = None


@dataclasses.dataclass
class DocPreviewPhotoSizes(
    ObjectBase,
):
    height: int
    src: str
    type: PhotoSizesType
    width: int


@dataclasses.dataclass
class DocPreviewVideo(
    ObjectBase,
):
    file_size: int
    height: int
    src: str
    width: int


@dataclasses.dataclass
class DocTypes(
    ObjectBase,
):
    count: int
    id: int
    name: str
