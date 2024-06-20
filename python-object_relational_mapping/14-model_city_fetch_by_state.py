#!/usr/bin/python3
"""deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
        )

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(City, State).join(State) \
        .order_by(City.id).all()
    
    for city, state in results:
        print(f'{state.name}: ({city.id}) {city.name}')
