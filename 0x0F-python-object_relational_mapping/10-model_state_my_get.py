#!/usr/bin/python3
"""
 - Write a script that prints the State object with the name passed as
   argument from the database hbtn_0e_6_usa

 - ✅ Your script should take 4 arguments: mysql username, mysql password,
   database name and state name to search **(SQL injection free)**
 - ✅ You must use the module SQLAlchemy
 - ✅ You must import State and Base from model_state - from model_state import
   Base, State
 - ✅ Your script should connect to a MySQL server running on localhost at port
   3306
 - ✅ You can assume you have one record with the state name to search
 - ✅ Results must display the states.id
 - ✅ If no state has the name you searched for, display Not found
 - ✅ Your code should not be executed when imported
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = Session().query(State).filter(State.name == argv[4])

    if (states.count()) > 0:
        print(states[0].id)
    else:
        print('Not found')
