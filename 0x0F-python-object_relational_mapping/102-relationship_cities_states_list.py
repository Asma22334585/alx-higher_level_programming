#!/usr/bin/python3
'''
lists all City objects from the database hbtn_0e_101_usa
'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        for x in instance.cities:
            print(x.id, x.name, sep=": ", end="")
            print(" -> " + instance.name)

    session.close()
    engine.close()
