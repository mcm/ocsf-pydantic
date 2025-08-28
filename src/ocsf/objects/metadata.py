from datetime import datetime
from typing import cast

from pydantic import create_model

from ocsf.objects.extension import Extension
from ocsf.objects.key_value_object import KeyValueObject
from ocsf.objects.logger import Logger
from ocsf.objects.object import Object
from ocsf.objects.product import Product
from ocsf.objects.transformation_info import TransformationInfo
from ocsf.profiles.data_classification import DataClassification


class Metadata(Object):
    # Required
    product: Product
    version: str

    # Recommended
    log_name: str | None = None
    log_provider: str | None = None
    original_time: str | None = None
    tenant_uid: str | None = None

    # Optional
    correlation_uid: str | None = None
    debug: list[str] | None = None
    event_code: str | None = None
    extension: Extension | None = None
    extensions: list[Extension] | None = None
    is_truncated: bool | None = None
    labels: list[str] | None = None
    log_level: str | None = None
    log_version: str | None = None
    logged_time: datetime | None = None
    loggers: list[Logger] | None = None
    modified_time: datetime | None = None
    processed_time: datetime | None = None
    profiles: list[str] | None = None
    sequence: int | None = None
    tags: list[KeyValueObject] | None = None
    transformation_info_list: list[TransformationInfo] | None = None
    uid: str | None = None
    untruncated_size: int | None = None

    @classmethod
    def with_profile(cls, profile: str) -> type["Metadata"]:
        if profile == "data_classification":
            return cast(
                type[Metadata],
                create_model("MetadataWithDataClassification", __base__=(Metadata, DataClassification)),
            )
        raise ValueError(f"Profile '{profile}' not available for Metadata")
