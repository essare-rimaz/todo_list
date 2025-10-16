from fastapi import APIRouter, Depends
from fastapi import status, HTTPException
from .authentication import get_current_user
from ..dependencies import get_db
from sqlalchemy.orm import Session
from ..schemas.projects import ProjectCreate, ProjectCreateResponse
from ...database import models

router = APIRouter(
    prefix="",
)

#TODO do I want to allow projects with the same name? Probably not...
@router.post("/projects", tags=["projects"], status_code=status.HTTP_201_CREATED, response_model=ProjectCreateResponse)
def post_project(
    item: ProjectCreate, 
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Create Project"
):
    '''
    Create a Project with an optional description
    '''
    project_name_exists = db.query(models.Project).filter(models.Project.project_name==item.project_name, models.Project.user_id_fk == user.id).first()
    if project_name_exists:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Project with this name already exists for this user"
        )
    
    db_item = models.Project(project_name=item.project_name, user_id_fk=user.id)    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/projects/{item_id}", tags=["projects"], status_code=status.HTTP_200_OK)
def delete_project(
    item_id: int, 
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    summary="Delete Project"
):
    '''
    Delete a Project
    '''
    record = db.query(models.Project).filter(
        models.Project.project_id == item_id, 
        models.TodoItem.user_id_fk == user.id
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(record)
    db.commit()
    return {"detail": "Item deleted successfully"}