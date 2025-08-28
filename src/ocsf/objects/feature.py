from ocsf.objects._entity import Entity


class Feature(Entity):
    # Recommended
    name: str | None = None
    uid: str | None = None
    version: str | None = None
