from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.process import Process


class ProcessQuery(DiscoveryResult):
    class_id: int = 5015
    class_name: str = "Process Query"

    # Required
    process: Process
