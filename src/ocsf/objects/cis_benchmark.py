from ocsf.objects.cis_control import CisControl
from ocsf.objects.object import Object


class CisBenchmark(Object):
    # Required
    name: str

    # Recommended
    cis_controls: list[CisControl] | None = None

    # Optional
    desc: str | None = None
