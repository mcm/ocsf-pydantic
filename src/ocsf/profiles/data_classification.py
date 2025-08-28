from pydantic import BaseModel

from ocsf.objects.data_classification import DataClassification as DataClassification_


class DataClassification(BaseModel):
    # Recommended
    data_classification: DataClassification_ | None = None
    data_classifications: list[DataClassification_] | None = None
