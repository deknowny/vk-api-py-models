import dataclasses
import enum
import typing

from vkmodels.bases.object import ObjectBase


class AccessRole(str, enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class AccessRolePublic(str, enum.Enum):
    MANAGER = "manager"
    REPORTS = "reports"


@dataclasses.dataclass
class Accesses(
    ObjectBase,
):
    client_id: typing.Optional[str] = None
    role: typing.Optional[AccessRole] = None


@dataclasses.dataclass
class Account(
    ObjectBase,
):
    access_role: AccessRole
    account_id: int
    account_name: str
    account_status: BoolInt
    account_type: AccountType
    can_view_budget: bool


class AccountType(str, enum.Enum):
    GENERAL = "general"
    AGENCY = "agency"


@dataclasses.dataclass
class Ad(
    ObjectBase,
):
    ad_format: int
    all_limit: int
    approved: AdApproved
    campaign_id: int
    cost_type: AdCostType
    id: int
    name: str
    status: AdStatus
    ad_platform: typing.Optional[typing.Union[int, str]] = None
    autobidding_max_cost: typing.Optional[int] = None
    category1_id: typing.Optional[int] = None
    category2_id: typing.Optional[int] = None
    cpa: typing.Optional[int] = None
    cpc: typing.Optional[int] = None
    cpm: typing.Optional[int] = None
    disclaimer_medical: typing.Optional[BoolInt] = None
    disclaimer_specialist: typing.Optional[BoolInt] = None
    disclaimer_supplements: typing.Optional[BoolInt] = None
    impressions_limit: typing.Optional[int] = None
    impressions_limited: typing.Optional[BoolInt] = None
    ocpm: typing.Optional[int] = None
    video: typing.Optional[BoolInt] = None


class AdApproved(int, enum.Enum):
    NOT_MODERATED = 0
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3


class AdCostType(int, enum.Enum):
    PER_CLICKS = 0
    PER_IMPRESSIONS = 1
    PER_ACTIONS = 2
    PER_IMPRESSIONS_OPTIMIZED = 3


@dataclasses.dataclass
class AdLayout(
    ObjectBase,
):
    ad_format: int
    campaign_id: int
    cost_type: AdCostType
    description: str
    id: str
    image_src: str
    link_url: str
    title: str
    image_src_2x: typing.Optional[str] = None
    link_domain: typing.Optional[str] = None
    preview_link: typing.Optional[str] = None
    video: typing.Optional[BoolInt] = None


class AdStatus(int, enum.Enum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


@dataclasses.dataclass
class Campaign(
    ObjectBase,
):
    all_limit: str
    day_limit: str
    id: int
    name: str
    start_time: int
    status: CampaignStatus
    stop_time: int
    type: CampaignType
    ads_count: typing.Optional[int] = None
    create_time: typing.Optional[int] = None
    goal_type: typing.Optional[int] = None
    is_cbo_enabled: typing.Optional[bool] = None
    update_time: typing.Optional[int] = None
    user_goal_type: typing.Optional[int] = None
    views_limit: typing.Optional[int] = None


class CampaignStatus(int, enum.Enum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class CampaignType(str, enum.Enum):
    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"
    ADAPTIVE_ADS = "adaptive_ads"
    STORIES = "stories"


@dataclasses.dataclass
class Category(
    ObjectBase,
):
    id: int
    name: str
    subcategories: typing.Optional[typing.List[ObjectWithName]] = None


@dataclasses.dataclass
class Client(
    ObjectBase,
):
    all_limit: str
    day_limit: str
    id: int
    name: str


@dataclasses.dataclass
class Criteria(
    ObjectBase,
):
    age_from: typing.Optional[int] = None
    age_to: typing.Optional[int] = None
    apps: typing.Optional[str] = None
    apps_not: typing.Optional[str] = None
    birthday: typing.Optional[int] = None
    cities: typing.Optional[str] = None
    cities_not: typing.Optional[str] = None
    country: typing.Optional[int] = None
    districts: typing.Optional[str] = None
    groups: typing.Optional[str] = None
    interest_categories: typing.Optional[str] = None
    interests: typing.Optional[str] = None
    paying: typing.Optional[BoolInt] = None
    positions: typing.Optional[str] = None
    religions: typing.Optional[str] = None
    retargeting_groups: typing.Optional[str] = None
    retargeting_groups_not: typing.Optional[str] = None
    school_from: typing.Optional[int] = None
    school_to: typing.Optional[int] = None
    schools: typing.Optional[str] = None
    sex: typing.Optional[CriteriaSex] = None
    stations: typing.Optional[str] = None
    statuses: typing.Optional[str] = None
    streets: typing.Optional[str] = None
    travellers: typing.Optional[PropertyExists] = None
    uni_from: typing.Optional[int] = None
    uni_to: typing.Optional[int] = None
    user_browsers: typing.Optional[str] = None
    user_devices: typing.Optional[str] = None
    user_os: typing.Optional[str] = None


class CriteriaSex(int, enum.Enum):
    ANY = 0
    MALE = 1
    FEMALE = 2


@dataclasses.dataclass
class DemoStats(
    ObjectBase,
):
    id: typing.Optional[int] = None
    stats: typing.Optional[DemostatsFormat] = None
    type: typing.Optional[ObjectType] = None


@dataclasses.dataclass
class DemostatsFormat(
    ObjectBase,
):
    age: typing.Optional[typing.List[StatsAge]] = None
    cities: typing.Optional[typing.List[StatsCities]] = None
    day: typing.Optional[str] = None
    month: typing.Optional[str] = None
    overall: typing.Optional[int] = None
    sex: typing.Optional[typing.List[StatsSex]] = None
    sex_age: typing.Optional[typing.List[StatsSexAge]] = None


@dataclasses.dataclass
class FloodStats(
    ObjectBase,
):
    left: int
    refresh: int


@dataclasses.dataclass
class LinkStatus(
    ObjectBase,
):
    description: str
    redirect_url: str
    status: str


@dataclasses.dataclass
class LookalikeRequest(
    ObjectBase,
):
    create_time: int
    id: int
    source_type: str
    status: str
    update_time: int
    audience_count: typing.Optional[int] = None
    save_audience_levels: typing.Optional[
        typing.List[LookalikeRequestSaveAudienceLevel]
    ] = None
    scheduled_delete_time: typing.Optional[int] = None
    source_name: typing.Optional[str] = None
    source_retargeting_group_id: typing.Optional[int] = None


@dataclasses.dataclass
class LookalikeRequestSaveAudienceLevel(
    ObjectBase,
):
    audience_count: typing.Optional[int] = None
    level: typing.Optional[int] = None


@dataclasses.dataclass
class Musician(
    ObjectBase,
):
    id: int
    name: str
    avatar: typing.Optional[str] = None


class ObjectType(str, enum.Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


@dataclasses.dataclass
class Paragraphs(
    ObjectBase,
):
    paragraph: typing.Optional[str] = None


@dataclasses.dataclass
class PromotedPostReach(
    ObjectBase,
):
    hide: int
    id: int
    join_group: int
    links: int
    reach_subscribers: int
    reach_total: int
    report: int
    to_group: int
    unsubscribe: int
    video_views_100p: typing.Optional[int] = None
    video_views_25p: typing.Optional[int] = None
    video_views_3s: typing.Optional[int] = None
    video_views_50p: typing.Optional[int] = None
    video_views_75p: typing.Optional[int] = None
    video_views_start: typing.Optional[int] = None


@dataclasses.dataclass
class RejectReason(
    ObjectBase,
):
    comment: typing.Optional[str] = None
    rules: typing.Optional[typing.List[Rules]] = None


@dataclasses.dataclass
class Rules(
    ObjectBase,
):
    paragraphs: typing.Optional[typing.List[Paragraphs]] = None
    title: typing.Optional[str] = None


@dataclasses.dataclass
class Stats(
    ObjectBase,
):
    id: typing.Optional[int] = None
    stats: typing.Optional[StatsFormat] = None
    type: typing.Optional[ObjectType] = None
    views_times: typing.Optional[StatsViewsTimes] = None


@dataclasses.dataclass
class StatsAge(
    ObjectBase,
):
    clicks_rate: typing.Optional[float] = None
    impressions_rate: typing.Optional[float] = None
    value: typing.Optional[str] = None


@dataclasses.dataclass
class StatsCities(
    ObjectBase,
):
    clicks_rate: typing.Optional[float] = None
    impressions_rate: typing.Optional[float] = None
    name: typing.Optional[str] = None
    value: typing.Optional[int] = None


@dataclasses.dataclass
class StatsFormat(
    ObjectBase,
):
    clicks: typing.Optional[int] = None
    day: typing.Optional[str] = None
    impressions: typing.Optional[int] = None
    join_rate: typing.Optional[int] = None
    link_external_clicks: typing.Optional[int] = None
    month: typing.Optional[str] = None
    overall: typing.Optional[int] = None
    reach: typing.Optional[int] = None
    spent: typing.Optional[int] = None
    video_clicks_site: typing.Optional[int] = None
    video_views: typing.Optional[int] = None
    video_views_full: typing.Optional[int] = None
    video_views_half: typing.Optional[int] = None


@dataclasses.dataclass
class StatsSex(
    ObjectBase,
):
    clicks_rate: typing.Optional[float] = None
    impressions_rate: typing.Optional[float] = None
    value: typing.Optional[StatsSexValue] = None


@dataclasses.dataclass
class StatsSexAge(
    ObjectBase,
):
    clicks_rate: typing.Optional[float] = None
    impressions_rate: typing.Optional[float] = None
    value: typing.Optional[str] = None


class StatsSexValue(str, enum.Enum):
    FEMALE = "f"
    MALE = "m"


@dataclasses.dataclass
class StatsViewsTimes(
    ObjectBase,
):
    views_ads_times_1: typing.Optional[int] = None
    views_ads_times_10: typing.Optional[int] = None
    views_ads_times_11_plus: typing.Optional[int] = None
    views_ads_times_2: typing.Optional[int] = None
    views_ads_times_3: typing.Optional[int] = None
    views_ads_times_4: typing.Optional[int] = None
    views_ads_times_5: typing.Optional[str] = None
    views_ads_times_6: typing.Optional[int] = None
    views_ads_times_7: typing.Optional[int] = None
    views_ads_times_8: typing.Optional[int] = None
    views_ads_times_9: typing.Optional[int] = None


@dataclasses.dataclass
class TargSettings(
    ObjectBase,
    Criteria,
):
    id: typing.Optional[int] = None
    campaign_id: typing.Optional[int] = None


@dataclasses.dataclass
class TargStats(
    ObjectBase,
):
    audience_count: int
    recommended_cpc: typing.Optional[float] = None
    recommended_cpc_50: typing.Optional[float] = None
    recommended_cpc_70: typing.Optional[float] = None
    recommended_cpc_90: typing.Optional[float] = None
    recommended_cpm: typing.Optional[float] = None
    recommended_cpm_50: typing.Optional[float] = None
    recommended_cpm_70: typing.Optional[float] = None
    recommended_cpm_90: typing.Optional[float] = None


@dataclasses.dataclass
class TargSuggestions(
    ObjectBase,
):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None


@dataclasses.dataclass
class TargSuggestionsCities(
    ObjectBase,
):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    parent: typing.Optional[str] = None


@dataclasses.dataclass
class TargSuggestionsRegions(
    ObjectBase,
):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    type: typing.Optional[str] = None


@dataclasses.dataclass
class TargSuggestionsSchools(
    ObjectBase,
):
    desc: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    parent: typing.Optional[str] = None
    type: typing.Optional[TargSuggestionsSchoolsType] = None


class TargSuggestionsSchoolsType(str, enum.Enum):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


@dataclasses.dataclass
class TargetGroup(
    ObjectBase,
):
    audience_count: typing.Optional[int] = None
    domain: typing.Optional[str] = None
    id: typing.Optional[int] = None
    lifetime: typing.Optional[int] = None
    name: typing.Optional[str] = None
    pixel: typing.Optional[str] = None


@dataclasses.dataclass
class UpdateOfficeUsersResult(
    ObjectBase,
):
    is_success: bool
    user_id: int
    error: typing.Optional[Error] = None


@dataclasses.dataclass
class UserSpecification(
    ObjectBase,
):
    role: AccessRolePublic
    user_id: int
    client_ids: typing.Optional[typing.List[int]] = None
    grant_access_to_all_clients: typing.Optional[bool] = False
    view_budget: typing.Optional[bool] = None


@dataclasses.dataclass
class UserSpecificationCutted(
    ObjectBase,
):
    role: AccessRolePublic
    user_id: int
    client_id: typing.Optional[int] = None
    view_budget: typing.Optional[bool] = None


@dataclasses.dataclass
class Users(
    ObjectBase,
):
    accesses: typing.List[Accesses]
    user_id: int
