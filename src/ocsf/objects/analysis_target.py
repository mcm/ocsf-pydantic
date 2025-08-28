from pydantic import BaseModel


class AnalysisTarget(BaseModel):
    # Required
    name: str

    # Optional
    type_: str | None = None
