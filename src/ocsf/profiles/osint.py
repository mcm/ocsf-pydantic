from pydantic import BaseModel

from ocsf.objects.osint import Osint as Osint_


class Osint(BaseModel):
    # Required
    osint: list[Osint_]
