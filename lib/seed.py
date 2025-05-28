from models.estate import Estate
from models.house import House

def seed():
    Estate.add_estate("Lion Park")
    Estate.add_estate("Green Court")

    House.add_house("1st Lane",1)
    House.add_house("2nd Lane",1)

    House.add_house("Groove park lane",2)
    House.add_house("Jim Street",2)

seed()
