from typing import Any

from ocsf.objects.object import Object


class Node(Object):
    # Required
    uid: str

    # Recommended
    name: str | None = None

    # Optional
    data: dict[str, Any] | None = None
    desc: str | None = None
    type_: str | None = None
