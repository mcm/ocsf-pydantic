from typing import Annotated, Literal

from pydantic import Field

from ocsf.events.base_event import BaseEvent


class Application(BaseEvent):
    category_name: Annotated[Literal["Application Activity"], Field(frozen=True)] = "Application Activity"
    category_uid: Annotated[Literal[6], Field(frozen=True)] = 6
