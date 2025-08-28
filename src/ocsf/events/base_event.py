from datetime import datetime
from enum import Enum, property as enum_property
from typing import Any, cast

from pydantic import BaseModel, create_model

from ocsf.objects.enrichment import Enrichment
from ocsf.objects.fingerprint import Fingerprint
from ocsf.objects.metadata import Metadata
from ocsf.objects.observable import Observable
from ocsf.profiles.cloud import Cloud
from ocsf.profiles.datetime import Datetime
from ocsf.profiles.host import Host
from ocsf.profiles.osint import Osint
from ocsf.profiles.security_control import SecurityControl


class ActivityId(Enum):
    UNKNOWN = 0
    OTHER = 99

    @classmethod
    def validate_python(cls, obj: Any):
        try:
            obj = int(obj)
        except ValueError:
            obj = str(obj).upper()
            return ActivityId[obj]
        else:
            return ActivityId(obj)

    @enum_property
    def name(self):
        name_map = {
            "UNKNOWN": "Unknown",
            "OTHER": "Other",
        }
        return name_map[super().name]


class SeverityId(Enum):
    UNKNOWN = 0
    INFORMATIONAL = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    CRITICAL = 5
    FATAL = 6
    OTHER = 99

    @classmethod
    def validate_python(cls, obj: Any):
        try:
            obj = int(obj)
        except ValueError:
            obj = str(obj).upper()
            return SeverityId[obj]
        else:
            return SeverityId(obj)

    @enum_property
    def name(self):
        name_map = {
            "UNKNOWN": "Unknown",
            "INFORMATIONAL": "Informational",
            "LOW": "Low",
            "MEDIUM": "Medium",
            "HIGH": "High",
            "CRITICAL": "Critical",
            "FATAL": "Fatal",
            "OTHER": "Other",
        }
        return name_map[super().name]


class StatusId(Enum):
    UNKNOWN = 0
    SUCCESS = 1
    FAILURE = 2
    OTHER = 99

    @classmethod
    def validate_python(cls, obj: Any):
        try:
            obj = int(obj)
        except ValueError:
            obj = str(obj).upper()
            return StatusId[obj]
        else:
            return StatusId(obj)

    @enum_property
    def name(self):
        name_map = {
            "UNKNOWN": "Unknown",
            "SUCCESS": "Success",
            "FAILURE": "Failure",
            "OTHER": "Other",
        }
        return name_map[super().name]


class BaseEvent(BaseModel):
    # Required
    activity_id: ActivityId
    category_uid: int = 0
    class_uid: int = 0
    metadata: Metadata
    severity_id: SeverityId
    time: datetime
    type_uid: int

    # Recommended
    message: str | None = None
    observables: list[Observable] | None = None
    status: str | None = None
    status_code: str | None = None
    status_detail: str | None = None
    status_id: StatusId | None = None
    timezone_offset: int | None = None

    # Optional
    activity_name: str | None = None
    category_name: str | None = None
    class_name: str | None = None
    count: int | None = None
    duration: int | None = None
    end_time: datetime | None = None
    enrichments: list[Enrichment] | None = None
    raw_data: str | None = None
    raw_data_hash: Fingerprint | None = None
    raw_data_size: int | None = None
    severity: str | None = None
    start_time: datetime | None = None
    type_name: str | None = None
    unmapped: dict[str, Any] | None = None

    @classmethod
    def with_profile(cls, profile: str) -> type["BaseEvent"]:
        if profile == "cloud":
            return cast(type[BaseEvent], create_model("BaseEventWithCloud", __base__=(BaseEvent, Cloud)))
        if profile == "datetime":
            return cast(
                type[BaseEvent], create_model("BaseEventWithDatetime", __base__=(BaseEvent, Datetime))
            )
        if profile == "host":
            return cast(type[BaseEvent], create_model("BaseEventWithHost", __base__=(BaseEvent, Host)))
        if profile == "osint":
            return cast(type[BaseEvent], create_model("BaseEventWithOsint", __base__=(BaseEvent, Osint)))
        if profile == "security_control":
            return cast(
                type[BaseEvent],
                create_model("BaseEventWithSecurityControl", __base__=(BaseEvent, SecurityControl)),
            )
        raise ValueError(f"Profile '{profile}' not available for BaseEvent")
