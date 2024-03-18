#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import Base, City
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

    joins = session.query(City, State).join(
        City, State.id == City.state_id).order_by(City.id).all()
    for hamza in joins:
        print("{}: ({}) {}".format(hamza[1].name, hamza[0].id, hamza[0].name))
    session.close()
