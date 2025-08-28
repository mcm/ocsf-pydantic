from typing import Annotated

from annotated_types import Ge, Lt

from ocsf.objects.object import Object


class PortInfo(Object):
    # Required
    port: Annotated[int, Ge(0), Lt(65536)]

    # Recommended
    protocol_name: str | None = None

    # Optional
    protocol_num: int | None = None
