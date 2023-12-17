#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
Your script should take 3 arguments: mysql
username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State
Results must be sorted in ascending order by cities.id
Results must be display in the following
format (<state name>: (<city id>) <city name>)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
