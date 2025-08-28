from datetime import datetime

from ocsf.objects.object import Object


class Epss(Object):
    # Required
    score: str

    # Recommended
    created_time: datetime | None = None
    version: str | None = None

    # Optional
    percentile: float | None = None
