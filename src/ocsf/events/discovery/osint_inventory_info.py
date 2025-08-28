from ocsf.events.discovery.discovery import Discovery
from ocsf.objects.actor import Actor
from ocsf.objects.osint import Osint


class OsintInventoryInfo(Discovery):
    class_id: int = 5021
    class_name: str = "OSINT Inventory Info"

    # Required
    osint: list[Osint]

    # Optional
    actor: Actor | None = None
