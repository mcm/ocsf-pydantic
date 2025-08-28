from ocsf.objects.object import Object


class CisCsc(Object):
    # Required
    control: str

    # Recommended
    version: str | None = None
