#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import create_engine, sessionmaker, Session
if __name__ == "__main__":
    conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2],
                                                       argv[3])
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
