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
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
