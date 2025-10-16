from ..database.connectivity import SessionLocal
from ..database import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()