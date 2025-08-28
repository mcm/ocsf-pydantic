from typing import Annotated, Literal, cast

from pydantic import Field, create_model, model_validator

from ocsf.events.base_event import BaseEvent
from ocsf.objects.ja4_fingerprint import Ja4Fingerprint
from ocsf.objects.network_connection_info import NetworkConnectionInfo
from ocsf.objects.network_endpoint import NetworkEndpoint
from ocsf.objects.network_proxy import NetworkProxy
from ocsf.objects.network_traffic import NetworkTraffic
from ocsf.objects.tls import TLS
from ocsf.profiles.load_balancer import LoadBalancer
from ocsf.profiles.network_proxy import NetworkProxy as NetworkProxy_


class Network(BaseEvent):
    category_name: Annotated[Literal["Network Activity"], Field(frozen=True)] = "Network Activity"
    category_uid: Annotated[Literal[4], Field(frozen=True)] = 4

    # Recommended
    connection_info: NetworkConnectionInfo | None = None
    dst_endpoint: NetworkEndpoint | None = None
    proxy: NetworkProxy | None = None
    src_endpoint: NetworkEndpoint | None = None
    traffic: NetworkTraffic | None = None

    # Optional
    app_name: str | None = None
    ja4_fingerprint_list: list[Ja4Fingerprint] | None = None
    tls: TLS | None = None

    @model_validator(mode="after")
    def validate_at_least_one(self):
        if all(getattr(self, field) is None for field in ["dst_endpoint", "src_endpoint"]):
            raise ValueError("At least one of `dst_endpoint`, `src_endpoint` must be provided")
        return self

    @classmethod
    def with_profile(cls, profile: str) -> type["Network"]:
        if profile == "network_proxy":
            return cast(
                type[Network], create_model("NetworkWithNetworkProxy", __base__=(Network, NetworkProxy_))
            )
        if profile == "load_balancer":
            return cast(
                type[Network], create_model("NetworkWithLoadBalancer", __base__=(Network, LoadBalancer))
            )
        raise ValueError(f"Profile '{profile}' not available for Network")
