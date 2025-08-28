from pydantic import BaseModel

from ocsf.objects.trace import Trace as Trace_


class Trace(BaseModel):
    # Recommended
    trace: Trace_ | None = None
