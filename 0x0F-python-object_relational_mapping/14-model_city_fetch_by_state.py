#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
