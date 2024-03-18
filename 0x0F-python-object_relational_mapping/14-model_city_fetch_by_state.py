#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import City
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    joins = session.query(City, State).\
        filter(City.state_id == State.id).all()
    for hamza, abdo in joins:
        print("{}: ({}) {}".format(abdo.name, hamza.id, hamza.name))
    session.commit()
    session.close()
