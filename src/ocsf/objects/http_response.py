from ocsf.objects.http_header import HttpHeader
from ocsf.objects.object import Object


class HttpResponse(Object):
    # Required
    code: int

    # Recommended
    http_headers: list[HttpHeader] | None = None

    # Optional
    body_length: int | None = None
    content_type: str | None = None
    latency: int | None = None
    length: int | None = None
    message: str | None = None
    status: str | None = None
