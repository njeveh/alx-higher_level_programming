#!/usr/bin/python3
'''contains  class definition of a City'''


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    ''' class definition of a City
        Attributes:
            id(int): An auto generated unique integer, can't
                     be null and is a pk
            name(str): The name of the state, max 128 chars and can't be null
            state_id(int): Foreign key to states.id can't be null
    '''

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
