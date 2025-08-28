from pydantic import AnyUrl

from ocsf.objects._entity import Entity
from ocsf.objects.d3fend import D3Fend


class Mitigation(Entity):
    # Recommended
    name: str | None = None
    uid: str | None = None

    # Optional
    countermeasures: list[D3Fend] | None = None
    src_url: AnyUrl | None = None
