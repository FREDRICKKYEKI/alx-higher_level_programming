#!/usr/bin/python3

"""
- Next, write a script 14-model_city_fetch_by_state.py that prints all City
  objects from the database hbtn_0e_14_usa:

- Your script should take 3 arguments: mysql username, mysql password and
  database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import
  Base, State
- Your script should connect to a MySQL server running on localhost at port
  3306
- Results must be sorted in ascending order by cities.id
- Results must be display as they are in the example below
  (<state name>: (<city id>) <city name>)
- Your code should not be executed when imported
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State,
                                             City.state_id == State.id).all()

    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
