from pydantic import BaseModel

from ocsf.objects.container import Container as Container_


class Container(BaseModel):
    # Recommended
    container: Container_ | None = None
    namespace_pid: int | None = None
