from fastapi import Depends, APIRouter

from typing import List

import schemas as schemas

router = APIRouter(
    prefix="",
)


@router.get("/my_endpoint", response_model=List[schemas.Testing_schema], tags=["something"])
def get_recommendations(
    isbn: str, 
    #db: Session = Depends(get_db),
    summary="Some future functionality"
):
    '''
    This probably does not do anything just yet but here will go more info
    '''

    return 'hello'

