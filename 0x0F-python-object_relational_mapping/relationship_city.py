#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:

    City class:
        No change
    State class:
        In addition to previous requirements, the class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
    You must use the module SQLAlchemy

Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)

    Your script should take 3 arguments: mysql username, mysql password and database name
    You must use the module SQLAlchemy
    Your script should connect to a MySQL server running on localhost at port 3306
    You must use the cities relationship for all State objects
    Your code should not be executed when imported
"""
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    City Class
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)