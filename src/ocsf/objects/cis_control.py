from ocsf.objects.object import Object


class CisControl(Object):
    # Required
    name: str

    # Recommended
    version: str | None = None

    # Optional
    desc: str | None = None
