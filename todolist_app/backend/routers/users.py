from typing import Annotated

from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .authentication import get_current_user
from ..schemas.users import User, UserCreate, ReturnUser
from ...database import models


router = APIRouter(
    prefix="",
)

@router.get("/users/me", tags=["users"])
def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user

@router.post("/users", tags=["users"], status_code=status.HTTP_201_CREATED)
def post_user(
    user: UserCreate,
    db: Session = Depends(get_db)
) -> ReturnUser:
    existing_user = db.query(models.User).filter(models.User.email==user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Email already registered"
        )
    
    new_user = models.User(email = user.email)
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.delete("/users", tags=["users"])
def delete_user(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # beware of cascade delete behaviour of TodoItems
    user = db.query(models.User).filter(models.User.id==user.id).first()

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}