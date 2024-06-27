from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP,text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.ext.declarative import declarative_base
from time import timezone


Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String,primary_key=False, nullable=False)
    content = Column(String,primary_key=False, nullable=False)
    status = Column(Enum("to_do", "in_progress", "done", name="status_enum"), nullable=False)
    description = Column(String,primary_key=False, nullable=True)
    owner_id = Column(Integer,ForeignKey('users.id', ondelete="CASCADE"),
                       primary_key=False, nullable=False)


class User(Base):
    __tablename__ = 'users'
    id =Column(Integer, primary_key=True,nullable=False)
    email =Column(String, nullable=False)
    password =Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),
                      nullable=False,server_default=text('now()'))