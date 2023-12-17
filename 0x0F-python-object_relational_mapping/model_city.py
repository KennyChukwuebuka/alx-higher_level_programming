#!/usr/bin/python3
"""Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City
City class:
    - inherits from Base (imported from model_state)
    - links to the MySQL table cities
    - class attributes:
        - id interger
        - name string
        - state_id integer
You must use the module SQLAlchemy
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class definition of a city for a MySQL database.

    Attributes:
        id (str): The city's id.
        name (Integer): The city's name.
        state_id (String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
