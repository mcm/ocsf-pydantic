from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.service import Service


class ServiceQuery(DiscoveryResult):
    class_id: int = 5016
    class_name: str = "Service Query"

    # Required
    service: Service
