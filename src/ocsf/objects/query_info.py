from datetime import datetime
from typing import Any

from ocsf.objects._entity import Entity


class QueryInfo(Entity):
    # Required
    query_string: str

    # Recommended
    name: str | None = None
    uid: str | None = None

    # Optional
    bytes: int | None = None
    data: dict[str, Any] | None = None
    query_time: datetime | None = None
