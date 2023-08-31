#!/usr/bin/python3
"""
Python file that contains the updated class definition of a City.
"""


from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


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
