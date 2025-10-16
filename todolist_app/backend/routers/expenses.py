from fastapi import Depends, APIRouter, status, HTTPException

from sqlalchemy.orm import Session

from ..dependencies import get_db
from .authentication import get_current_user
from ...database import models
from ..schemas.expenses import ExpenseCreateResponse, ExpenseCreate

router = APIRouter(
    prefix="",
)

@router.post("/expenses", tags=["expenses"], status_code=status.HTTP_201_CREATED, response_model=ExpenseCreateResponse)
def post_expense_item(
    item: ExpenseCreate, 
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Create ExpenseItem"
):
    '''
    Create a ExpenseItem with an optional description
    '''

    db_item = models.Expense(
        expense_name = item.expense_name,
        expense_frequency = item.expense_frequency,
        #TODO the API let me insert string into an INT column of a database
        expense_amount = item.expense_amount,
        currency = item.currency,
        user_id_fk = user.id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

@router.delete("/expenses/{item_id}", tags=["expenses"], status_code=status.HTTP_200_OK)
def delete_expense_item(
    item_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Delete ExpenseItem"
):
    '''
    Delete given ExpenseItem
    '''
    record = db.query(models.Expense).filter(
        models.Expense.inventory_id == item_id, 
        models.Expense.user_id_fk == user.id
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(record)
    db.commit()
    return {"detail": "Item deleted successfully"}