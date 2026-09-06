from typing import Literal

from pydantic import BaseModel, Field


class PassengerInput(BaseModel):
    age: float = Field(gt=0, le=100)
    sex: Literal["male", "female"]
