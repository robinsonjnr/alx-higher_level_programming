#!/usr/bin/python3
"""
a script that lists all City objects from the database hbtn_0e_101_usa

    Your script should take 3 arguments: mysql username, mysql password and database name
    You must use the module SQLAlchemy
    Your script should connect to a MySQL server running on localhost at port 3306
    You must use only one query to the database
    You must use the state relationship to access to the State object linked to the City object
    Results must be sorted in ascending order by cities.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State):
        for city in state.cities:
            print("{:d}: {} -> {}".format(city.id, city.name, state.name))
    session.close()