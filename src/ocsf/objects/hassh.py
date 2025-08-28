from ocsf.objects.fingerprint import Fingerprint
from ocsf.objects.object import Object


class Hassh(Object):
    # Required
    fingerprint: Fingerprint

    # Recommended
    algorithm: str | None = None
