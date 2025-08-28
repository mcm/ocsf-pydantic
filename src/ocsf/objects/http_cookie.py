from datetime import datetime

from ocsf.objects.object import Object


class HttpCookie(Object):
    # Required
    name: str
    value: str

    # Optional
    domain: str | None = None
    expiration_time: datetime | None = None
    http_only: bool | None = None
    is_http_only: bool | None = None
    is_secure: bool | None = None
    path: str | None = None
    samesite: str | None = None
    secure: bool | None = None
