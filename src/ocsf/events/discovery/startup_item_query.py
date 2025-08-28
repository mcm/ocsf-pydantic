from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.startup_item import StartupItem


class StartupItemQuery(DiscoveryResult):
    class_id: int = 5022
    class_name: str = "Startup Item Query"

    # Required
    startup_item: StartupItem
