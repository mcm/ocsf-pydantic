from pydantic import BaseModel

from ocsf.objects.load_balancer import LoadBalancer as LoadBalancer_


class LoadBalancer(BaseModel):
    # Recommended
    load_balancer: LoadBalancer_ | None = None
