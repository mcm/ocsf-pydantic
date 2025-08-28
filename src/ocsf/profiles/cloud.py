from pydantic import BaseModel

from ocsf.objects.api import API
from ocsf.objects.cloud import Cloud as Cloud_


class Cloud(BaseModel):
    # Required
    cloud: Cloud_

    # Optional
    api: API | None = None
