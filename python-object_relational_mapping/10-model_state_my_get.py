#!/usr/bin/python3
"""prints the State object with the name
 passed as argument from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
        )

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == state_name) \
        .first()

    if state:
        print(f'{state.id}')
    else:
        print("Not found")
