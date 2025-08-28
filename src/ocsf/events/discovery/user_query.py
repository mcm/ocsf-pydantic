from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.user import User


class UserQuery(DiscoveryResult):
    class_id: int = 5018
    class_name: str = "User Query"

    # Required
    user: User
