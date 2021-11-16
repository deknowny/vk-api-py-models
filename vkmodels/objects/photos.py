import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class Image(
    ObjectBase,
):
    height: typing.Optional[int] = None
    type: typing.Optional[ImageType] = None
    url: typing.Optional[str] = None
    width: typing.Optional[int] = None


class ImageType(str, enum.Enum):
    S = "s"
    M = "m"
    X = "x"
    L = "l"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"


@dataclasses.dataclass
class Photo(
    ObjectBase,
):
    album_id: int
    date: int
    has_tags: bool
    id: int
    owner_id: int
    access_key: typing.Optional[str] = None
    can_comment: typing.Optional[BoolInt] = None
    height: typing.Optional[int] = None
    images: typing.Optional[typing.List[Image]] = None
    lat: typing.Optional[float] = None
    long: typing.Optional[float] = None
    photo_256: typing.Optional[str] = None
    place: typing.Optional[str] = None
    post_id: typing.Optional[int] = None
    sizes: typing.Optional[typing.List[PhotoSizes]] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class PhotoAlbum(
    ObjectBase,
):
    created: int
    id: int
    owner_id: int
    size: int
    title: str
    updated: int
    description: typing.Optional[str] = None
    thumb: typing.Optional[Photo] = None


@dataclasses.dataclass
class PhotoAlbumFull(
    ObjectBase,
):
    created: int
    id: int
    owner_id: int
    size: int
    title: str
    updated: int
    can_upload: typing.Optional[BoolInt] = None
    comments_disabled: typing.Optional[BoolInt] = None
    description: typing.Optional[str] = None
    sizes: typing.Optional[typing.List[PhotoSizes]] = None
    thumb_id: typing.Optional[int] = None
    thumb_is_last: typing.Optional[BoolInt] = None
    thumb_src: typing.Optional[str] = None
    upload_by_admins_only: typing.Optional[BoolInt] = None


PhotoFalseable: typing.TypeAlias = typing.Union[
    bool,
    str,
]


@dataclasses.dataclass
class PhotoFull(
    ObjectBase,
):
    album_id: int
    date: int
    id: int
    owner_id: int
    access_key: typing.Optional[str] = None
    can_comment: typing.Optional[BoolInt] = None
    comments: typing.Optional[ObjectCount] = None
    height: typing.Optional[int] = None
    images: typing.Optional[typing.List[Image]] = None
    lat: typing.Optional[float] = None
    likes: typing.Optional[Likes] = None
    long: typing.Optional[float] = None
    post_id: typing.Optional[int] = None
    reposts: typing.Optional[RepostsInfo] = None
    tags: typing.Optional[ObjectCount] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class PhotoFullXtrRealOffset(
    ObjectBase,
):
    album_id: int
    date: int
    id: int
    owner_id: int
    access_key: typing.Optional[str] = None
    can_comment: typing.Optional[BoolInt] = None
    comments: typing.Optional[ObjectCount] = None
    height: typing.Optional[int] = None
    hidden: typing.Optional[PropertyExists] = None
    lat: typing.Optional[float] = None
    likes: typing.Optional[Likes] = None
    long: typing.Optional[float] = None
    photo_1280: typing.Optional[str] = None
    photo_130: typing.Optional[str] = None
    photo_2560: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None
    photo_75: typing.Optional[str] = None
    photo_807: typing.Optional[str] = None
    post_id: typing.Optional[int] = None
    real_offset: typing.Optional[int] = None
    reposts: typing.Optional[ObjectCount] = None
    sizes: typing.Optional[typing.List[PhotoSizes]] = None
    tags: typing.Optional[ObjectCount] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class PhotoSizes(
    ObjectBase,
):
    height: int
    type: PhotoSizesType
    url: str
    width: int
    src: typing.Optional[str] = None


class PhotoSizesType(str, enum.Enum):
    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    K = "k"
    L = "l"
    Y = "y"
    Z = "z"
    C = "c"
    W = "w"
    A = "a"
    B = "b"
    E = "e"
    I = "i"
    D = "d"
    J = "j"
    TEMP = "temp"
    H = "h"
    G = "g"
    N = "n"
    F = "f"
    MAX = "max"


@dataclasses.dataclass
class PhotoTag(
    ObjectBase,
):
    date: int
    id: int
    placer_id: int
    tagged_name: str
    user_id: int
    viewed: BoolInt
    x: float
    x2: float
    y: float
    y2: float
    description: typing.Optional[str] = None


@dataclasses.dataclass
class PhotoUpload(
    ObjectBase,
):
    album_id: int
    upload_url: str
    user_id: int
    fallback_upload_url: typing.Optional[str] = None
    group_id: typing.Optional[int] = None


@dataclasses.dataclass
class PhotoXtrRealOffset(
    ObjectBase,
):
    album_id: int
    date: int
    id: int
    owner_id: int
    access_key: typing.Optional[str] = None
    height: typing.Optional[int] = None
    hidden: typing.Optional[PropertyExists] = None
    lat: typing.Optional[float] = None
    long: typing.Optional[float] = None
    photo_1280: typing.Optional[str] = None
    photo_130: typing.Optional[str] = None
    photo_2560: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None
    photo_75: typing.Optional[str] = None
    photo_807: typing.Optional[str] = None
    post_id: typing.Optional[int] = None
    real_offset: typing.Optional[int] = None
    sizes: typing.Optional[typing.List[PhotoSizes]] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class PhotoXtrTagInfo(
    ObjectBase,
):
    album_id: int
    date: int
    id: int
    owner_id: int
    access_key: typing.Optional[str] = None
    height: typing.Optional[int] = None
    lat: typing.Optional[float] = None
    long: typing.Optional[float] = None
    photo_1280: typing.Optional[str] = None
    photo_130: typing.Optional[str] = None
    photo_2560: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None
    photo_75: typing.Optional[str] = None
    photo_807: typing.Optional[str] = None
    placer_id: typing.Optional[int] = None
    post_id: typing.Optional[int] = None
    sizes: typing.Optional[typing.List[PhotoSizes]] = None
    tag_created: typing.Optional[int] = None
    tag_id: typing.Optional[int] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


@dataclasses.dataclass
class TagsSuggestionItem(
    ObjectBase,
):
    buttons: typing.Optional[typing.List[TagsSuggestionItemButton]] = None
    caption: typing.Optional[str] = None
    photo: typing.Optional[Photo] = None
    tags: typing.Optional[typing.List[PhotoTag]] = None
    title: typing.Optional[str] = None
    track_code: typing.Optional[str] = None
    type: typing.Optional[str] = None


@dataclasses.dataclass
class TagsSuggestionItemButton(
    ObjectBase,
):
    action: typing.Optional[str] = None
    style: typing.Optional[str] = None
    title: typing.Optional[str] = None
