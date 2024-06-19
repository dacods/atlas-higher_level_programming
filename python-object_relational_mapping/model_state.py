#!/usr/bin/python3
"""contains the class definition of a State
and an instance Base = declarative_base()"""
from sqlalchmey import Column, Integer, String
from sqlalchmey.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """Defines a class"""
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)

    name = Column(String(128), nullable=False)
