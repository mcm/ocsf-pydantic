from pydantic import model_validator

from ocsf.objects.object import Object


class KeyValueObject(Object):
    # Required
    name: str

    # Recommended
    value: str | None = None
    values: list[str] | None = None

    @model_validator(mode="after")
    def validate_at_least_one(self):
        if all(getattr(self, field) is None for field in ["value", "values"]):
            raise ValueError("At least one of `value`, `values` must be provided")
        return self
