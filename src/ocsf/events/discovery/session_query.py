from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.session import Session


class SessionQuery(DiscoveryResult):
    class_id: int = 5017
    class_name: str = "User Session Query"

    # Required
    session: Session
