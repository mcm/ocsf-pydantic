from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.network_interface import NetworkInterface


class NetworksQuery(DiscoveryResult):
    class_id: int = 5013
    class_name: str = "Networks Query"

    # Required
    network_interfaces: list[NetworkInterface]
