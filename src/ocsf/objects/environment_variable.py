from ocsf.objects.object import Object


class EnvironmentVariable(Object):
    # Required
    name: str
    value: str
