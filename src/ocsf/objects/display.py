from ocsf.objects.object import Object


class Display(Object):
    # Optional
    color_depth: int | None = None
    physical_height: int | None = None
    physical_orientation: int | None = None
    physical_width: int | None = None
    scale_factor: int | None = None
