from enum import Enum, property as enum_property
from typing import Any

from pydantic import AnyUrl, BaseModel

from ocsf.objects.group import Group
from ocsf.objects.ticket import Ticket
from ocsf.objects.user import User


class ImpactId(Enum):
    UNKNOWN = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
    OTHER = 99

    @classmethod
    def validate_python(cls, obj: Any):
        try:
            obj = int(obj)
        except ValueError:
            obj = str(obj).upper()
            return ImpactId[obj]
        else:
            return ImpactId(obj)

    @enum_property
    def name(self):
        name_map = {
            "UNKNOWN": "Unknown",
            "LOW": "Low",
            "MEDIUM": "Medium",
            "HIGH": "High",
            "CRITICAL": "Critical",
            "OTHER": "Other",
        }
        return name_map[super().name]


class PriorityId(Enum):
    UNKNOWN = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
    OTHER = 99

    @classmethod
    def validate_python(cls, obj: Any):
        try:
            obj = int(obj)
        except ValueError:
            obj = str(obj).upper()
            return PriorityId[obj]
        else:
            return PriorityId(obj)

    @enum_property
    def name(self):
        name_map = {
            "UNKNOWN": "Unknown",
            "LOW": "Low",
            "MEDIUM": "Medium",
            "HIGH": "High",
            "CRITICAL": "Critical",
            "OTHER": "Other",
        }
        return name_map[super().name]


class VerdictId(Enum):
    UNKNOWN = 0
    FALSE_POSITIVE = 1
    TRUE_POSITIVE = 2
    DISREGARD = 3
    SUSPICIOUS = 4
    BENIGN = 5
    TEST = 6
    INSUFFICIENT_DATA = 7
    SECURITY_RISK = 8
    MANAGED_EXTERNALLY = 9
    DUPLICATE = 10
    OTHER = 99

    @classmethod
    def validate_python(cls, obj: Any):
        try:
            obj = int(obj)
        except ValueError:
            obj = str(obj).upper()
            return VerdictId[obj]
        else:
            return VerdictId(obj)

    @enum_property
    def name(self):
        name_map = {
            "UNKNOWN": "Unknown",
            "FALSE_POSITIVE": "False Positive",
            "TRUE_POSITIVE": "True Positive",
            "DISREGARD": "Disregard",
            "SUSPICIOUS": "Suspicious",
            "BENIGN": "Benign",
            "TEST": "Test",
            "INSUFFICIENT_DATA": "Insufficient Data",
            "SECURITY_RISK": "Security Risk",
            "MANAGED_EXTERNALLY": "Managed Externally",
            "DUPLICATE": "Duplicate",
            "OTHER": "Other",
        }
        return name_map[super().name]


class Incident(BaseModel):
    # Recommended
    impact: str | None = None
    impact_id: ImpactId | None = None
    impact_score: int | None = None
    priority_id: PriorityId | None = None
    src_url: AnyUrl | None = None
    verdict: str | None = None
    verdict_id: VerdictId | None = None

    # Optional
    assignee: User | None = None
    assignee_group: Group | None = None
    is_suspected_breach: bool | None = None
    priority: str | None = None
    ticket: Ticket | None = None
    tickets: list[Ticket] | None = None
