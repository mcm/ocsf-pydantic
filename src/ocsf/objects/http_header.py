from ocsf.objects.object import Object


class HttpHeader(Object):
    # Required
    name: str
    value: str
