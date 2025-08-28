from ocsf.objects.object import Object
from ocsf.objects.occurrence_details import OccurrenceDetails


class DiscoveryDetails(Object):
    # Recommended
    count: int | None = None
    type_: str | None = None

    # Optional
    occurrence_details: OccurrenceDetails | None = None
    occurrences: list[OccurrenceDetails] | None = None
    value: str | None = None
