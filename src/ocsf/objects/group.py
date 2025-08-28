from ocsf.objects._entity import Entity


class Group(Entity):
    # Recommended
    name: str | None = None
    uid: str | None = None

    # Optional
    desc: str | None = None
    domain: str | None = None
    privileges: list[str] | None = None
    type_: str | None = None
