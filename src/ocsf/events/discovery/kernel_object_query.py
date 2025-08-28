from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.kernel import Kernel


class KernelObjectQuery(DiscoveryResult):
    class_id: int = 5006
    class_name: str = "Kernel Object Query"

    # Required
    kernel: Kernel
