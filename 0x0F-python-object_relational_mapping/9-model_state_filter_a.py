#!/usr/bin/python3
"""script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql
username, mysql password and database name
You must import State and Base from
model_state - from model_state import Base, State
Results must be sorted in ascending order by states.id
You must use the module SQLAlchemy
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
    session.close()
