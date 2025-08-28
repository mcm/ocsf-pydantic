from datetime import datetime

from ocsf.objects.fingerprint import Fingerprint
from ocsf.objects.object import Object
from ocsf.objects.san import San


class Certificate(Object):
    # Required
    issuer: str
    serial_number: str

    # Recommended
    created_time: datetime | None = None
    expiration_time: datetime | None = None
    fingerprints: list[Fingerprint] | None = None
    is_self_signed: bool | None = None
    subject: str | None = None
    version: str | None = None

    # Optional
    sans: list[San] | None = None
    uid: str | None = None
