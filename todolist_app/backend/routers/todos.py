from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from ..dependencies import get_db
from .authentication import get_current_user
from ...database import models
from ..schemas.todos import ItemCreate, ItemPatch, ItemCreateResponse
from ..docs.todos import post_todo_example_1
from typing import Annotated

router = APIRouter(
    prefix="",
)

@router.post("/todos", tags=["todos"], status_code=status.HTTP_201_CREATED, response_model=ItemCreateResponse)
def post_todo_item(
    item: Annotated[ItemCreate, post_todo_example_1], 
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Create TodoItem"
):
    '''
    Create a TodoItem with an optional description
    '''
    project_belongs_to_user = db.query(models.Project).filter(models.Project.project_id == item.project_id, models.Project.user_id_fk == user.id).first()
    if (item.project_id is None) or ((isinstance(item.project_id, int)) and project_belongs_to_user):
    #if project_id_exists:
        db_item = models.TodoItem(name=item.name, description=item.description, project_id=item.project_id, user_id_fk=user.id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)

    elif not project_belongs_to_user:
            raise HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail="This project_id does not exist for this user"
    )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="did not expect this to happen"
    )

    return db_item

#TODO when is it 200 or 204?
@router.get("/todos", tags=["todos"], status_code=status.HTTP_200_OK)
def get_todo_item(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Get TodoItems"
):
    '''
    Get all TodoItems
    '''
    all_rows = db.query(models.TodoItem).filter(models.TodoItem.user_id_fk == user.id).all()

    if all_rows == []:
        return JSONResponse(status_code=204, content=None)

    return all_rows


@router.delete("/todos/{item_id}", tags=["todos"], status_code=status.HTTP_200_OK)
def delete_todo_item(
    item_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Delete TodoItem"
):
    '''
    Delete given TodoItem
    '''
    record = db.query(models.TodoItem).filter(
        models.TodoItem.id == item_id, 
        models.TodoItem.user_id_fk == user.id
    ).first()

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
    user: models.User = Depends(get_current_user),
    summary="Patch TodoItem"
):
    record = db.query(models.TodoItem).filter(
        models.TodoItem.id == item_id, 
        models.TodoItem.user_id_fk == user.id
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data_dict = item.model_dump(exclude_unset=True) # Exclude fields not provided in the patch request
    for key, value in update_data_dict.items():
        setattr(record, key, value)
    
    db.commit()
    db.refresh(record)
    return record