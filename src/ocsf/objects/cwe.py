from pydantic import AnyUrl

from ocsf.objects.object import Object


class Cwe(Object):
    # Required
    uid: str

    # Optional
    caption: str | None = None
    src_url: AnyUrl | None = None
