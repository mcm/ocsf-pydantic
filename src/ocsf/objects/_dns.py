from ocsf.objects.object import Object


class Dns(Object):
    # Recommended
    class_: str | None = None
    packet_uid: int | None = None
    type_: str | None = None
