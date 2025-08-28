from ocsf.objects._entity import Entity
from ocsf.objects.key_value_object import KeyValueObject


class Image(Entity):
    # Required
    uid: str

    # Recommended
    name: str | None = None

    # Optional
    labels: list[str] | None = None
    path: str | None = None
    tag: str | None = None
    tags: list[KeyValueObject] | None = None
