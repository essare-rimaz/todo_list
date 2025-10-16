from pydantic import BaseModel
from datetime import date
from pydantic_extra_types.currency_code import ISO4217


# seperate owe money and owe object?
# lets say, that owing me objects is a "lend" so a different endpoint
class OweCreate(BaseModel):
    owe_name: str
    who_owes: str
    owe_deadline: date|None = None #TODO should be CET by default
    how_much: int #TODO should be bigger than 0
    currency: ISO4217 = 'CZK'


class OweCreateResponse(BaseModel):
    owe_id: int
    owe_name: str
    user_id_fk: int

    class Config:
        orm_mode: True