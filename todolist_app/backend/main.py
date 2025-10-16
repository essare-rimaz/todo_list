from fastapi import FastAPI
from .routers import todos, users, authentication, projects, owes, inventory, expenses

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
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(projects.router)
app.include_router(owes.router)
app.include_router(inventory.router)
app.include_router(expenses.router)