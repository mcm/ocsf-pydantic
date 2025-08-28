from ocsf.objects.object import Object


class ClassifierDetails(Object):
    # Required
    type_: str

    # Recommended
    name: str | None = None
    uid: str | None = None
