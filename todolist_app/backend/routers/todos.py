from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from .. import schemas
from ..dependencies import get_db, models


router = APIRouter(
    prefix="",
)


class ItemCreate(BaseModel):
    name: str
    description: str|None = None

class ItemPatch(BaseModel):
    name: str|None = None
    description: str|None = None

class ItemCreateResponse(BaseModel):
    name: str
    description: str|None
    id: int

    class Config:
        orm_mode: True


@router.post("/todos", tags=["todos"], status_code=status.HTTP_201_CREATED, response_model=ItemCreateResponse)
def post_todo_item(
    item: ItemCreate, 
    db: Session = Depends(get_db),
    summary="Create TodoItem"
):
    '''
    Create a TodoItem with an optional description
    '''
    db_item = models.TodoItem(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

@router.get("/todos", tags=["todos"], status_code=status.HTTP_200_OK)
def get_todo_item(
    db: Session = Depends(get_db),
    summary="Get TodoItems"
):
    '''
    Get all TodoItems
    '''
    all_rows = db.query(models.TodoItem).all()

    if all_rows == []:
        return JSONResponse(status_code=204, content=None)

    return all_rows


@router.delete("/todos/{item_id}", tags=["todos"], status_code=status.HTTP_200_OK)
def delete_todo_item(
    item_id: int,
    db: Session = Depends(get_db),
    summary="Delete TodoItem"
):
    '''
    Delete given TodoItem
    '''
    record = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(record)
    db.commit()
    return {"detail": "Item deleted successfully"}


@router.patch("/todos/{item_id}", tags=["todos"], status_code=status.HTTP_200_OK)
def patch_todo_item(
    item_id: int,
    item: ItemPatch,
    db: Session = Depends(get_db),
    summary="Patch TodoItem"
):
    record = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data_dict = item.model_dump(exclude_unset=True) # Exclude fields not provided in the patch request
    for key, value in update_data_dict.items():
        setattr(record, key, value)
    
    db.commit()
    db.refresh(record)
    return record