from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str|None = None
    project_id: int | None = None

class ItemPatch(BaseModel):
    name: str|None = None
    description: str|None = None

class ItemCreateResponse(BaseModel):
    name: str
    description: str|None
    id: int
    project_id: int|None

    class Config:
        orm_mode: True
