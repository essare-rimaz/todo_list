from fastapi import Depends, APIRouter, status, HTTPException

from sqlalchemy.orm import Session

from ..dependencies import get_db
from .authentication import get_current_user
from ...database import models
from ..schemas.inventory import InventoryCreateResponse, InventoryCreate

router = APIRouter(
    prefix="",
)

@router.post("/inventories", tags=["inventory"], status_code=status.HTTP_201_CREATED, response_model=InventoryCreateResponse)
def post_inventory_item(
    item: InventoryCreate, 
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Create InventoryItem"
):
    '''
    Create a InventoryItem with an optional description
    '''

    db_item = models.Inventory(
        inventory_name = item.inventory_name,
        cost = item.cost,
        currency = item.currency,
        photo = item.photo,
        receipt = item.receipt,
        purchase_date = item.purchase_date,
        warranty = item.warranty,
        user_id_fk = user.id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

@router.delete("/inventories/{item_id}", tags=["inventory"], status_code=status.HTTP_200_OK)
def delete_inventory_item(
    item_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Delete InventoryItem"
):
    '''
    Delete given InventoryItem
    '''
    record = db.query(models.Inventory).filter(
        models.Inventory.inventory_id == item_id, 
        models.Inventory.user_id_fk == user.id
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(record)
    db.commit()
    return {"detail": "Item deleted successfully"}