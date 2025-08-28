from ocsf.events.remediation.remediation_activity import RemediationActivity
from ocsf.objects.process import Process


class ProcessRemediationActivity(RemediationActivity):
    class_id: int = 7003
    class_name: str = "Process Remediation Activity"

    # Required
    process: Process
