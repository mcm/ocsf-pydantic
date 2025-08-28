from typing import cast

from pydantic import AnyUrl, create_model

from ocsf.objects._entity import Entity
from ocsf.objects.feature import Feature
from ocsf.profiles.data_classification import DataClassification


class Product(Entity):
    # Recommended
    name: str | None = None
    uid: str | None = None
    vendor_name: str | None = None
    version: str | None = None

    # Optional
    cpe_name: str | None = None
    feature: Feature | None = None
    lang: str | None = None
    path: str | None = None
    url_string: AnyUrl | None = None

    @classmethod
    def with_profile(cls, profile: str) -> type["Product"]:
        if profile == "data_classification":
            return cast(
                type[Product],
                create_model("ProductWithDataClassification", __base__=(Product, DataClassification)),
            )
        raise ValueError(f"Profile '{profile}' not available for Product")
