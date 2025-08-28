from typing import Any

from ocsf.objects.container import Container
from ocsf.objects.object import Object


class Request(Object):
    # Required
    uid: str

    # Optional
    containers: list[Container] | None = None
    data: dict[str, Any] | None = None
    flags: list[str] | None = None
