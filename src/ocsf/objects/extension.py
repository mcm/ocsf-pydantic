from ocsf.objects._entity import Entity


class Extension(Entity):
    # Required
    name: str
    uid: str
    version: str
