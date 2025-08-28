from typing import cast

from pydantic import EmailStr, IPvAnyAddress, create_model, model_validator

from ocsf.objects.file import File
from ocsf.objects.http_header import HttpHeader
from ocsf.objects.object import Object
from ocsf.objects.url import Url
from ocsf.profiles.data_classification import DataClassification


class Email(Object):
    # Recommended
    from_: EmailStr | None = None
    message_uid: str | None = None
    reply_to: EmailStr | None = None
    size: int | None = None
    smtp_from: EmailStr | None = None
    smtp_to: list[EmailStr] | None = None
    subject: str | None = None
    to: list[EmailStr] | None = None
    uid: str | None = None

    # Optional
    cc: list[EmailStr] | None = None
    cc_mailboxes: list[str] | None = None
    delivered_to: EmailStr | None = None
    delivered_to_list: list[EmailStr] | None = None
    files: list[File] | None = None
    from_list: list[EmailStr] | None = None
    from_mailbox: str | None = None
    from_mailboxes: list[EmailStr] | None = None
    http_headers: list[HttpHeader] | None = None
    is_read: bool | None = None
    raw_header: str | None = None
    reply_to_list: list[EmailStr] | None = None
    reply_to_mailboxes: list[str] | None = None
    return_path: EmailStr | None = None
    sender: EmailStr | None = None
    sender_mailbox: str | None = None
    to_mailboxes: list[str] | None = None
    urls: list[Url] | None = None
    x_originating_ip: list[IPvAnyAddress] | None = None

    @model_validator(mode="after")
    def validate_at_least_one(self):
        if all(getattr(self, field) is None for field in ["from", "to"]):
            raise ValueError("At least one of `from`, `to` must be provided")
        return self

    @classmethod
    def with_profile(cls, profile: str) -> type["Email"]:
        if profile == "data_classification":
            return cast(
                type[Email], create_model("EmailWithDataClassification", __base__=(Email, DataClassification))
            )
        raise ValueError(f"Profile '{profile}' not available for Email")
