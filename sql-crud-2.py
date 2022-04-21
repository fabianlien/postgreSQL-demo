from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()


class IceCreamFlavor(base):
    __tablename__ = "Ice Cream Flavors"
    id = Column(Integer, primary_key=True)
    flavor = Column(String)
    allergens = Column(String)
    kcal_per_100g = Column(Integer, primary_key=False)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Class instances:
vanilla = IceCreamFlavor(
    flavor="Vanilla",
    allergens="egg, dairy",
    kcal_per_100g="343"
)

raspberry_sorbet = IceCreamFlavor(
    flavor="Raspberry Sorbet",
    allergens="Raspberry",
    kcal_per_100g="187"
)

#session.add(raspberry_sorbet)

#session.query(IceCreamFlavor).filter_by(id=2).first().flavor = "Chocolate"
#session.query(IceCreamFlavor).filter_by(id=2).first().kcal_per_100g = 326
session.commit()
