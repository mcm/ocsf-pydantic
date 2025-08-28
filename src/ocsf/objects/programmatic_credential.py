from datetime import datetime

from ocsf.objects.object import Object


class ProgrammaticCredential(Object):
    # Required
    uid: str

    # Recommended
    type_: str | None = None

    # Optional
    last_used_time: datetime | None = None
