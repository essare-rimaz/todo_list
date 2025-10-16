from pydantic import BaseModel, Field
from datetime import date
from pydantic_extra_types.currency_code import ISO4217
from datetime import date

class ExpenseCreate(BaseModel):
    expense_name: str
    expense_frequency: str
    expense_amount: int
    currency: str = 'CZK'

class ExpenseCreateResponse(BaseModel):
    expense_name: str

    class Config:
        orm_mode: True