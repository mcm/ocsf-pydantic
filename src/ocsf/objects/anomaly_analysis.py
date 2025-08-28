from pydantic import BaseModel

from ocsf.objects.analysis_target import AnalysisTarget
from ocsf.objects.anomaly import Anomaly
from ocsf.objects.baseline import Baseline


class AnomalyAnalysis(BaseModel):
    # Required
    analysis_targets: list[AnalysisTarget]
    anomalies: list[Anomaly]

    # Recommended
    baselines: list[Baseline] | None = None
