from pydantic import model_validator

from ocsf.objects.mitigation import Mitigation
from ocsf.objects.object import Object
from ocsf.objects.sub_technique import SubTechnique
from ocsf.objects.tactic import Tactic
from ocsf.objects.technique import Technique


class Attack(Object):
    # Recommended
    sub_technique: SubTechnique | None = None
    tactic: Tactic | None = None
    technique: Technique | None = None
    version: str | None = None

    # Optional
    mitigation: Mitigation | None = None
    tactics: list[Tactic] | None = None

    @model_validator(mode="after")
    def validate_at_least_one(self):
        if all(getattr(self, field) is None for field in ["tactic", "technique", "sub_technique"]):
            raise ValueError("At least one of `tactic`, `technique`, `sub_technique` must be provided")
        return self
