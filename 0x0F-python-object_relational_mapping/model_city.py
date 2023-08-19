#!/usr/bin/python3

"""
Write a Python file similar to model_state.py named model_city.py that
contains the class definition of a City.
 - City class:
    - inherits from Base (imported from model_state)
    - links to the MySQL table cities
    - class attribute id that represents a column of an auto-generated,
      unique integer, can't be null and is a primary key
    - class attribute name that represents a column of a string of 128
      characters and can't be null
    - class attribute state_id that represents a column of an integer, can't
      be null and is a foreign key to states.id
 - You must use the module SQLAlchemy
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """cities (table) class definition\n
    `CREATE TABLE IF NOT EXISTS cities` (
        `id` `INT` `NOT` `NULL` `AUTO_INCREMENT`,\n
        `state_id` `INT` `NOT` `NULL`,\n
        `name` `VARCHAR(256)` `NOT` `NULL`,\n
        `PRIMARY KEY(id)`,\n
        `FOREIGN KEY(state_id)` `REFERENCES states(id)`\n
    );
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(256), nullable=False)
