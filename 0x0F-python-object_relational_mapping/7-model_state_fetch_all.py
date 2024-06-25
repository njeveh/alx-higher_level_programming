#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import create_engine, Session
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
            ), pool_pre_ping=True)
    session = Session(bind=engine)
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(state)
