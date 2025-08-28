from ocsf.objects.object import Object
from ocsf.objects.remediation import Remediation
from ocsf.objects.rule import Rule


class CisBenchmarkResult(Object):
    # Required
    name: str

    # Optional
    desc: str | None = None
    remediation: Remediation | None = None
    rule: Rule | None = None
