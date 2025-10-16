from fastapi import FastAPI

#from database.db import engine

#from database import models

from .routers import todos as todos

#models.Base.metadata.create_all(engine)

tags_metadata = [
    {
        "name": "todos",
        "description": "endpoint related to todo items",
    },
]

description = '''
This is a small todolist app
'''

app = FastAPI(
    title="TODOlist app",
    version="0.0.1",
    description=description,
    openapi_tags=tags_metadata
    )

app.include_router(todos.router)