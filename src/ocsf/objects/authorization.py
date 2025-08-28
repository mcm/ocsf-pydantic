from ocsf.objects.object import Object
from ocsf.objects.policy import Policy


class Authorization(Object):
    # Recommended
    decision: str | None = None

    # Optional
    policy: Policy | None = None
