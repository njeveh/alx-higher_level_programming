#!/usr/bin/python3
"""Contains a script that lists all State objects from the database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    eng = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                                      sys.argv[3])
    engine = create_engine(eng)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]) \
                   .order_by(State.id).first()

    if state:
        print(state.id)
    else:
        print("Not found")
