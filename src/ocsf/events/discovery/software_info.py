from ocsf.events.discovery.discovery import Discovery
from ocsf.objects.actor import Actor
from ocsf.objects.device import Device
from ocsf.objects.package import Package
from ocsf.objects.product import Product
from ocsf.objects.sbom import Sbom


class SoftwareInfo(Discovery):
    class_id: int = 5020
    class_name: str = "Software Inventory Info"

    # Required
    device: Device

    # Recommended
    package: Package | None = None
    sbom: Sbom | None = None

    # Optional
    actor: Actor | None = None
    product: Product | None = None
