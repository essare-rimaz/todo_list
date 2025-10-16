from sqlalchemy.orm import Mapped
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column
from .connectivity import Base
from sqlalchemy import Identity

class TodoItem(Base):
    __tablename__ = 'todo_item'

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=True)

''' optional for debugging
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
'''