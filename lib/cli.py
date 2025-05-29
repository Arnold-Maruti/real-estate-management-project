from functions import add_a_house,add_estate,buy_a_house,see_available_houses,remove_a_house,remove_an_estate,search_for_clients_in_estate,estates


def agent_menu():
    print("Which of the following functions would you like to perform our dear agent:")
    print("1)Adding a house")
    print("2)Add a new estate")
    print("3)See my estates")
    print("4)Go back to the main page to change user")
    print("5)Exit the application")

def agent():
    while True:
        agent_menu()
        choice=input(">")
        if choice=="1":
            print("Enter the house location")
            x=input(">")
            print("Enter estate_id")
            y=input(">")
            add_a_house(x,y)
        elif choice=="2":
            print("Enter estate name")
            r=input(">")
            add_estate(r)
        elif choice=="3":
            estates()
        elif choice=="4":
            main_menu()
        elif choice=="5":
            print("Thank you for using our system")
            exit()
        else:
            print("Invalid choice entered")


        

def client():
    print("i am a client")


def main_menu():
    print("Welcome to my real estate management system.To enter the system choose one of the following user")
    print("1:Agent")
    print("2:Client")
    x=input(">")

    if x=="1":
       agent()
    else:
        client()

main_menu()