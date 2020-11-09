from sqlalchemy import (
    Column, Integer, ForeignKey,
    Boolean, Text, DateTime
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Text, primary_key=True)
    create_date = Column(DateTime)


class Board(Base):
    __tablename__ = "board"
    id = Column(Text, primary_key=True)
    user_id = Column(Text, ForeignKey("user.id"))
    create_date = Column(DateTime)


class List(Base):
    __tablename__ = "list"
    id = Column(Text, primary_key=True)
    board_id = Column(Text, ForeignKey("board.id"))
    closed = Column(Boolean)
    open = Column(Boolean)
    name = Column(Text)
    pos = Column(Integer)
    subscribed = Column(Boolean)
    create_date = Column(DateTime)


class Card(Base):
    __tablename__ = "card"
    id = Column(Text, primary_key=True)
    start_list_id = Column(Text, ForeignKey("list.id"))
    finish_list_id = Column(Text, ForeignKey("list.id"))
    name = Column(Text)
    pos = Column(Integer)
    description = Column(Text)
    due_date = Column(DateTime)
    short_url = Column(Text)
    url = Column(Text)
    cadence = Column(Text)
    closed = Column(Boolean)
    member_id = Column(Text)
    create_date = Column(DateTime)
    edit_date = Column(DateTime)
    is_due_complete = Column(Boolean)


class Activity(Base):
    __tablename__ = 'activity'
    id = Column(Text, primary_key=True)
    card_id = Column(Text, ForeignKey("card.id"))
    list_id = Column(Text, ForeignKey("list.id"))
    list_before = Column(Text)
    list_after = Column(Text)
    create_date = Column(DateTime)
