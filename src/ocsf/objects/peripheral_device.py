from ocsf.objects._entity import Entity


class PeripheralDevice(Entity):
    # Required
    class_: str
    name: str

    # Recommended
    model: str | None = None
    serial_number: str | None = None
    uid: str | None = None
    vendor_name: str | None = None
