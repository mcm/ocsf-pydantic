from typing import Any

from ocsf.objects._entity import Entity


class Edge(Entity):
    # Required
    source: str
    target: str

    # Recommended
    name: str | None = None
    relation: str | None = None
    uid: str | None = None

    # Optional
    data: dict[str, Any] | None = None
    is_directed: bool | None = None
