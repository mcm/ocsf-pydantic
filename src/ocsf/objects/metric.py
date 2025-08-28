from ocsf.objects.object import Object


class Metric(Object):
    # Required
    name: str
    value: str
