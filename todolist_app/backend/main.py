from fastapi import FastAPI

#from database.db import engine

#from database import models

import schemas as schemas

from routers import my_endpoint

#models.Base.metadata.create_all(engine)

tags_metadata = [
    {
        "name": "something",
        "description": "placeholder text",
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

app.include_router(my_endpoint.router)