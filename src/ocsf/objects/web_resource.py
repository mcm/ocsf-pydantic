from typing import Any

from pydantic import AnyUrl

from ocsf.objects._resource import Resource


class WebResource(Resource):
    # Recommended
    name: str | None = None
    uid: str | None = None
    url_string: AnyUrl | None = None

    # Optional
    data: dict[str, Any] | None = None
    desc: str | None = None
    type_: str | None = None
