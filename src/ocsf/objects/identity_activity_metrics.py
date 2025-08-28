from datetime import datetime

from ocsf.objects.object import Object
from ocsf.objects.programmatic_credential import ProgrammaticCredential


class IdentityActivityMetrics(Object):
    # Recommended
    last_seen_time: datetime | None = None

    # Optional
    first_seen_time: datetime | None = None
    last_authentication_time: datetime | None = None
    password_last_used_time: datetime | None = None
    programmatic_credentials: list[ProgrammaticCredential] | None = None
