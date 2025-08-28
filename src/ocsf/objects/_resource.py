from datetime import datetime
from typing import Any, cast

from pydantic import create_model

from ocsf.objects._entity import Entity
from ocsf.objects.key_value_object import KeyValueObject
from ocsf.profiles.data_classification import DataClassification


class Resource(Entity):
    # Recommended
    name: str | None = None
    uid: str | None = None

    # Optional
    created_time: datetime | None = None
    data: dict[str, Any] | None = None
    labels: list[str] | None = None
    modified_time: datetime | None = None
    tags: list[KeyValueObject] | None = None
    type_: str | None = None
    uid_alt: str | None = None

    @classmethod
    def with_profile(cls, profile: str) -> type["Resource"]:
        if profile == "data_classification":
            return cast(
                type[Resource],
                create_model("ResourceWithDataClassification", __base__=(Resource, DataClassification)),
            )
        raise ValueError(f"Profile '{profile}' not available for Resource")
