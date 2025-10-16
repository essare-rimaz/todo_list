from pydantic import BaseModel, Field, EmailStr
from typing_extensions import Annotated
from typing import Union

class Testing_schema(BaseModel):
    ID: int
    NAME: str
    DESCRIPTION: str