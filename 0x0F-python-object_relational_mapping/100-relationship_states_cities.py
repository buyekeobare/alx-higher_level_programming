#!/usr/bin/python3

"""
This module connects python script to a database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    add_state = State(name='California')
    add_city = City(name="San Francisco", state=add_state)
    session.add(add_state, add_city)
    session.commit()

    session.close()
