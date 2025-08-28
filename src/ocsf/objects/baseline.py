from ocsf.objects.object import Object
from ocsf.objects.observation import Observation


class Baseline(Object):
    # Required
    observation_parameter: str
    observations: list[Observation]

    # Recommended
    observation_type: str | None = None
    observed_pattern: str | None = None
