from typing import Any

from pydantic import BaseModel, Field, ValidationError, validator
from pydantic.main import ModelMetaclass


class Test(BaseModel):
    age_1: int = Field(alias='textlll')
    age_2: int = Field(0, gt=10, lt=50)
    age_3: int

    @validator('age_1', allow_reuse=True)
    @validator('age_3', allow_reuse=True)
    # @validator('age_4', allow_reuse=True, check_fields=False)
    def check_name_length(cls, v):
        assert v < 20, 'error-----%s'
        return v


class CustomVerify:
    @staticmethod
    def verify_dict(model: ModelMetaclass, data: dict) -> Any:
        try:
            model(**data)
        except ValidationError as e:
            key = e.raw_errors[0]._loc
            error_msg = str(e.raw_errors[0].exc)
            return error_msg % key


a = {
    'age_1': 1,
    'age_2': 20,
    'age_3': 1,
}
print(CustomVerify.verify_dict(Test, a))
