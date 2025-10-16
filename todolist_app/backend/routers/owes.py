from fastapi import Depends, APIRouter, status

from sqlalchemy.orm import Session

from ..dependencies import get_db
from .authentication import get_current_user
from ...database import models
from ..schemas.owes import OweCreateResponse, OweCreate

router = APIRouter(
    prefix="",
)

@router.post("/owes", tags=["owes"], status_code=status.HTTP_201_CREATED, response_model=OweCreateResponse)
def post_owes_item(
    item: OweCreate, 
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Create OwesItem"
):
    '''
    Create a OwesItem with an optional description
    '''

    db_item = models.Owe(
        owe_name=item.owe_name, 
        who_owes=item.who_owes, 
        owe_deadline=item.owe_deadline, 
        how_much=item.how_much, 
        currency=item.currency, 
        user_id_fk=user.id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item