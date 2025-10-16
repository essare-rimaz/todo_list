from sqlalchemy.orm import Mapped
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column
from .connectivity import Base
from sqlalchemy import Identity
from passlib.context import CryptContext
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List


# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class TodoItem(Base):
    __tablename__ = 'todo_item'

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True, nullable=False, autoincrement=True)
    # when cascade delete is not set, SQLAlchemy tries to dessociate the item by setting the user_id_fk to NULL which will fail unless set to nullable=True
    # https://docs.sqlalchemy.org/en/20/orm/cascades.html#delete
    # ideally I would like to set the cascade option
    # there seems to be a lot to digest regarding how SQLAlchemy, cascade delete and relation databases integrate
    # https://docs.sqlalchemy.org/en/20/orm/cascades.html#using-foreign-key-on-delete-cascade-with-orm-relationships
    user_id_fk: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    users: Mapped["User"] = relationship(back_populates="todo_items")
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=True)

''' optional for debugging
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
'''

class User(Base):
    __tablename__= 'user'

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True, nullable=False, autoincrement=True)
    email: Mapped[str] = mapped_column(String(256), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)

    todo_items: Mapped[List["TodoItem"]] = relationship(back_populates="users", cascade="all, delete")

    def set_password(self, password):
        self.hashed_password = pwd_context.hash(password)