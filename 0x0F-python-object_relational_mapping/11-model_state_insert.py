#!/usr/bin/python3
"""
A script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa.
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(
        name='Louisiana'
    )
    session.add(state)
    session.commit()
    print("{}".format(state.id))
