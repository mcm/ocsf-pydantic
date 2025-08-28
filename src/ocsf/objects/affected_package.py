from ocsf.objects.package import Package
from ocsf.objects.remediation import Remediation


class AffectedPackage(Package):
    # Optional
    fixed_in_version: str | None = None
    path: str | None = None
    remediation: Remediation | None = None
