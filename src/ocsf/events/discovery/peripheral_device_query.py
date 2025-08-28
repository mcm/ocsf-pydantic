from ocsf.events.discovery.discovery_result import DiscoveryResult
from ocsf.objects.peripheral_device import PeripheralDevice


class PeripheralDeviceQuery(DiscoveryResult):
    class_id: int = 5014
    class_name: str = "Peripheral Device Query"

    # Required
    peripheral_device: PeripheralDevice
