from pydantic import BaseModel

class ProjectCreate(BaseModel):
    project_name: str


class ProjectCreateResponse(BaseModel):
    project_id: int
    project_name: str
    user_id_fk: int

    class Config:
        orm_mode: True
