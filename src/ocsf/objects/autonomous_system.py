from pydantic import model_validator

from ocsf.objects.object import Object


class AutonomousSystem(Object):
    # Recommended
    name: str | None = None
    number: int | None = None

    @model_validator(mode="after")
    def validate_at_least_one(self):
        if all(getattr(self, field) is None for field in ["number", "name"]):
            raise ValueError("At least one of `number`, `name` must be provided")
        return self
