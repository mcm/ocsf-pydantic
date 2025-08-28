from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.file import File


class FileQuery(DiscoveryResult):
    class_id: int = 5007
    class_name: str = "File Query"

    # Required
    file: File
