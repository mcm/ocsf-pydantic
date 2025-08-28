from enum import Enum, property as enum_property
from typing import Any, cast

from pydantic import create_model

from ocsf.events.network.network import Network
from ocsf.objects.network_endpoint import NetworkEndpoint
from ocsf.objects.network_interface import NetworkInterface
from ocsf.profiles.cloud import Cloud


class ActivityId(Enum):
    UNKNOWN = 0
    DISCOVER = 1
    OFFER = 2
    REQUEST = 3
    DECLINE = 4
    ACK = 5
    NAK = 6
    RELEASE = 7
    INFORM = 8
    EXPIRE = 9
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
            "DISCOVER": "Discover",
            "OFFER": "Offer",
            "REQUEST": "Request",
            "DECLINE": "Decline",
            "ACK": "Ack",
            "NAK": "Nak",
            "RELEASE": "Release",
            "INFORM": "Inform",
            "EXPIRE": "Expire",
            "OTHER": "Other",
        }
        return name_map[super().name]


class DhcpActivity(Network):
    class_id: int = 4004
    class_name: str = "DHCP Activity"

    # Required
    activity_id: ActivityId

    # Recommended
    dst_endpoint: NetworkEndpoint | None = None
    is_renewal: bool | None = None
    lease_dur: int | None = None
    relay: NetworkInterface | None = None
    src_endpoint: NetworkEndpoint | None = None
    transaction_uid: str | None = None

    @classmethod
    def with_profile(cls, profile: str) -> type["DhcpActivity"]:
        if profile == "cloud":
            return cast(
                type[DhcpActivity], create_model("DhcpActivityWithCloud", __base__=(DhcpActivity, Cloud))
            )
        raise ValueError(f"Profile '{profile}' not available for DhcpActivity")
