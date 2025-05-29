from models.estate import Estate
from models.house import House

# functions from Estate class
def add_estate(name):
    Estate.add_estate(name)

def remove_an_estate(id):
    Estate.remove_estate(id)

def search_for_clients_in_estate(id):
    print(Estate.clients_in_estate(id))

def estates():
    print(Estate.show_my_estates())


# functions from House class
def add_a_house(location,estate_id):
    House.add_house(location,estate_id)

def see_available_houses():
    print(House.see_available_houses())

def remove_a_house(id):
    House.demolish_house(id)

def buy_a_house(name,location):
    House.buy_house(name,location)
