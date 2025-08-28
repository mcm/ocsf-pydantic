from ocsf.objects.object import Object


class LongString(Object):
    # Required
    value: str

    # Optional
    is_truncated: bool | None = None
    untruncated_size: int | None = None
