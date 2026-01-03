from fastapi import FastAPI
from .routers import todos, users, authentication, projects, owes, inventory, expenses
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:5173",
]

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router)
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(projects.router)
app.include_router(owes.router)
app.include_router(inventory.router)
app.include_router(expenses.router)