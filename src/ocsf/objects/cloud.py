from ocsf.objects.account import Account
from ocsf.objects.object import Object
from ocsf.objects.organization import Organization


class Cloud(Object):
    # Required
    provider: str

    # Recommended
    region: str | None = None

    # Optional
    account: Account | None = None
    cloud_partition: str | None = None
    org: Organization | None = None
    project_uid: str | None = None
    zone: str | None = None
