from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///todolist_app/database/todo_app.db")
print(engine.url.database)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)