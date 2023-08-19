#!/usr/bin/python3

"""
- Python module that contains the updated class definition of a State.
- State class:
    - In addition to previous requirements, the class attribute cities must
      represent a relationship with the class City.
      - If the State object is deleted, all linked City objects must be
        automatically deleted.
      - Also, the reference from a City object to his State should be
        named state
- You must use the module SQLAlchemy
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """class that defines a State\n
    `CREATE TABLE IF NOT EXISTS states` (\n
        `id` `INT` `NOT` `NULL` `AUTO_INCREMENT`,\n
        `name` `VARCHAR(256)` `NOT` `NULL`,\n
        `PRIMARY KEY(id)`\n
    );\n
    Has relationship with cities
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)
    cities = relationship("City", backref='states')
