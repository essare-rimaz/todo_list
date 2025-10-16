from pydantic import BaseModel, Field
from datetime import date
from pydantic_extra_types.currency_code import ISO4217
from datetime import date
from dateutil.relativedelta import relativedelta


class InventoryCreate(BaseModel):
    inventory_name: str
    cost: float = Field(gt=0, description="The cost must be greater than zero")
    currency: str = 'CZK'
    photo: str|None = None
    receipt: str|None = None
    purchase_date: date = date.today
    warranty: int = Field(default=2, ge=1, description="The warranty must at least one year")

class InventoryCreateResponse(BaseModel):
    inventory_name: str

    class Config:
        orm_mode: True