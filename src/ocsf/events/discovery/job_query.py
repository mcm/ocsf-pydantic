from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.job import Job


class JobQuery(DiscoveryResult):
    class_id: int = 5010
    class_name: str = "Job Query"

    # Required
    job: Job
