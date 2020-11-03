from sqlalchemy import (
    Column, Integer, ForeignKey,
    Boolean, Text, DateTime
)
from sqlalchemy.ext.declarative import declarative_base


Model = declarative_base()


class User(Model):
    __tablename__ = "user"
    id = Column(Text, primary_key=True)
    create_date = Column(DateTime)


class Board(Model):
    __tablename__ = "board"
    id = Column(Text, primary_key=True)
    user_id = Column(Text, ForeignKey("user.id"))
    create_date = Column(DateTime)


class List(Model):
    __tablename__ = "list"
    id = Column(Text, primary_key=True)
    board_id = Column(Text, ForeignKey("board.id"))
    closed = Column(Boolean)
    open = Column(Boolean)
    name = Column(Text)
    pos = Column(Integer)
    subscribed = Column(Boolean)
    create_date = Column(DateTime)


class Card(Model):
    __tablename__ = "card"
    id = Column(Text, primary_key=True)
    card_id = Column(Text, ForeignKey("state.id"))
    list_id = Column(Text, ForeignKey("list.id"))
    name = Column(Text)
    pos = Column(Integer)
    description = Column(Text)
    due_date = Column(DateTime)
    short_url = Column(Text)
    url = Column(Text)
    cadence = Column(Text)
    closed = Column(Boolean)
    member_id = Column()
    create_date = Column(DateTime)
    edit_date = Column(DateTime)
    is_due_complete = Column(Boolean)
