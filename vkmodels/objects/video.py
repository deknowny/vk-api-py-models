import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


@dataclasses.dataclass
class LiveInfo(
    ObjectBase,
):
    enabled: BoolInt
    is_notifications_blocked: typing.Optional[BoolInt] = None


@dataclasses.dataclass
class LiveSettings(
    ObjectBase,
):
    can_rewind: typing.Optional[BoolInt] = None
    is_endless: typing.Optional[BoolInt] = None
    max_duration: typing.Optional[int] = None


@dataclasses.dataclass
class SaveResult(
    ObjectBase,
):
    access_key: typing.Optional[str] = None
    description: typing.Optional[str] = None
    owner_id: typing.Optional[int] = None
    title: typing.Optional[str] = None
    upload_url: typing.Optional[str] = None
    video_id: typing.Optional[int] = None


@dataclasses.dataclass
class Video(
    ObjectBase,
):
    access_key: typing.Optional[str] = None
    adding_date: typing.Optional[int] = None
    can_comment: typing.Optional[BoolInt] = None
    can_edit: typing.Optional[BoolInt] = None
    can_like: typing.Optional[BoolInt] = None
    can_repost: typing.Optional[BoolInt] = None
    can_subscribe: typing.Optional[BoolInt] = None
    can_add_to_faves: typing.Optional[BoolInt] = None
    can_add: typing.Optional[BoolInt] = None
    can_attach_link: typing.Optional[BoolInt] = None
    is_private: typing.Optional[BoolInt] = None
    comments: typing.Optional[int] = None
    date: typing.Optional[int] = None
    description: typing.Optional[str] = None
    duration: typing.Optional[int] = None
    image: typing.Optional[typing.List[VideoImage]] = None
    first_frame: typing.Optional[typing.List[VideoImage]] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    user_id: typing.Optional[int] = None
    title: typing.Optional[str] = None
    is_favorite: typing.Optional[bool] = None
    player: typing.Optional[str] = None
    processing: typing.Optional[PropertyExists] = None
    converting: typing.Optional[BoolInt] = None
    added: typing.Optional[BoolInt] = None
    is_subscribed: typing.Optional[BoolInt] = None
    track_code: typing.Optional[str] = None
    repeat: typing.Optional[PropertyExists] = None
    type: typing.Optional[str] = None
    views: typing.Optional[int] = None
    local_views: typing.Optional[int] = None
    content_restricted: typing.Optional[int] = None
    content_restricted_message: typing.Optional[str] = None
    balance: typing.Optional[int] = None
    live_status: typing.Optional[str] = None
    live: typing.Optional[PropertyExists] = None
    upcoming: typing.Optional[PropertyExists] = None
    live_start_time: typing.Optional[int] = None
    live_notify: typing.Optional[BoolInt] = None
    spectators: typing.Optional[int] = None
    platform: typing.Optional[str] = None
    likes: typing.Optional[Likes] = None
    reposts: typing.Optional[RepostsInfo] = None


@dataclasses.dataclass
class VideoAlbum(
    ObjectBase,
):
    id: int
    owner_id: int
    title: str


@dataclasses.dataclass
class VideoAlbumFull(
    ObjectBase,
    VideoAlbum,
):
    count: typing.Optional[int] = None
    image: typing.Optional[typing.List[VideoImage]] = None
    image_blur: typing.Optional[PropertyExists] = None
    is_system: typing.Optional[PropertyExists] = None
    updated_time: typing.Optional[int] = None


@dataclasses.dataclass
class VideoFiles(
    ObjectBase,
):
    external: typing.Optional[str] = None
    flv_320: typing.Optional[str] = None
    mp4_1080: typing.Optional[str] = None
    mp4_1440: typing.Optional[str] = None
    mp4_2160: typing.Optional[str] = None
    mp4_240: typing.Optional[str] = None
    mp4_360: typing.Optional[str] = None
    mp4_480: typing.Optional[str] = None
    mp4_720: typing.Optional[str] = None


@dataclasses.dataclass
class VideoFull(
    ObjectBase,
    Video,
):
    files: typing.Optional[VideoFiles] = None
    live_settings: typing.Optional[LiveSettings] = None


@dataclasses.dataclass
class VideoImage(
    ObjectBase,
    Image,
):
    with_padding: typing.Optional[PropertyExists] = None
