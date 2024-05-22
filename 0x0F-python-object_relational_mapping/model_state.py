#!/usr/bin/python3
''' contains the class definition of a State and
an instance Base = declarative_base()'''

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''A model for states that links to the MySQL table
    states
    Attributes:
        id(str): An auto generated unique integer, can't be null and is a pk
        name(str): The name of the state, max 128 chars and can't be null
    '''

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
