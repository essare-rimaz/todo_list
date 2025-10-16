from sqlalchemy.orm import Mapped
from sqlalchemy import String, Integer, Date, Float
from sqlalchemy.orm import mapped_column
from .connectivity import Base
from sqlalchemy import Identity
from passlib.context import CryptContext
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List
from datetime import date
from pydantic_extra_types.currency_code import ISO4217
from dateutil.relativedelta import relativedelta
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
    project_id: Mapped[int] = mapped_column(ForeignKey("project.project_id", ondelete="CASCADE"), nullable=True)
    projects: Mapped["Project"] = relationship(back_populates="todo_items")

''' optional for debugging
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
'''

class User(Base):
    __tablename__= 'user'

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True, nullable=False, autoincrement=True)
    email: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)

    todo_items: Mapped[List["TodoItem"]] = relationship(back_populates="users", cascade="all, delete")
    projects: Mapped[List["Project"]] = relationship(back_populates="users", cascade="all, delete")
    owes: Mapped[List["Owe"]] = relationship(back_populates="users", cascade="all, delete")
    inventories: Mapped[List["Inventory"]] = relationship(back_populates="users", cascade="all, delete")
    expenses: Mapped[List["Expense"]] = relationship(back_populates="users", cascade="all, delete")


    def set_password(self, password):
        self.hashed_password = pwd_context.hash(password)

class Project(Base):
    __tablename__= 'project'

    project_id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True, nullable=False, autoincrement=True)
    project_name: Mapped[str] = mapped_column(String(256), nullable=False)

    todo_items: Mapped[List["TodoItem"]] = relationship(back_populates="projects", cascade="all, delete")
    
    user_id_fk: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    users: Mapped["User"] = relationship(back_populates="projects")


class Owe(Base):
    __tablename__= 'owe'

    owe_id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True, nullable=False, autoincrement=True)
    owe_name: Mapped[str] = mapped_column(String(256), nullable=False)
    who_owes: Mapped[str] = mapped_column(String(256), nullable=False)
    owe_deadline: Mapped[date] = mapped_column((Date), nullable=True)
    how_much: Mapped[int] = mapped_column(Integer, nullable=False)
    #TODO can be turned to ISO4217
    currency: Mapped[str] = mapped_column(String(256), nullable=False)

    user_id_fk: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    users: Mapped["User"] = relationship(back_populates="owes")


def get_warranty_end_date(context):
    purchase_date = context.get_current_parameters()['purchase_date']
    warranty = context.get_current_parameters()['warranty']
    return purchase_date + relativedelta(years=warranty)


class Inventory(Base):
    __tablename__= 'inventory'

    inventory_id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True, nullable=False, autoincrement=True)
    inventory_name: Mapped[str] = mapped_column(String(256), nullable=False)
    
    cost: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(256), nullable=False)

    # how to store photos? https://stackoverflow.com/questions/3748/storing-images-in-db-yea-or-nay
    # could be path to the image, but then the question is - how will the image make it to the filesystem in the first place...
    photo: Mapped[str] = mapped_column(String(256), nullable=True)
    receipt: Mapped[str] = mapped_column((String(256)), nullable=True)

    purchase_date: Mapped[date] = mapped_column(Date, nullable=False)
    warranty: Mapped[int] = mapped_column(Integer, nullable=True) # it seems warranty is always in years
    # https://stackoverflow.com/questions/36579355/sqlalchemy-set-default-value-of-one-column-to-that-of-another-column
    warranty_end_date: Mapped[date] = mapped_column(Date, nullable=True, default=get_warranty_end_date)
    
    user_id_fk: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    users: Mapped["User"] = relationship(back_populates="inventories")

class Expense(Base):
    __tablename__= 'expenses'

    expense_id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True, nullable=False, autoincrement=True)
    expense_name: Mapped[str] = mapped_column(String(256), nullable=False)
    expense_frequency: Mapped[str] = mapped_column(String(256), nullable=False)
    expense_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    #TODO can be turned to ISO4217
    currency: Mapped[str] = mapped_column(String(256), nullable=False)

    user_id_fk: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    users: Mapped["User"] = relationship(back_populates="expenses")