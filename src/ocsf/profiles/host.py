from pydantic import BaseModel

from ocsf.objects.actor import Actor
from ocsf.objects.device import Device


class Host(BaseModel):
    # Recommended
    device: Device | None = None

    # Optional
    actor: Actor | None = None
