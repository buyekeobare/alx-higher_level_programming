#!/usr/bin/python3

"""
This module connects python script to a database
"""



from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    This is class definines the state class"""
    """

    __tablename__ = "states"
    id = Column(Integer(), primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete")
