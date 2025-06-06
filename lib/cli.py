from functions import add_a_house,add_estate,buy_a_house,see_available_houses,remove_a_house,remove_an_estate,search_for_clients_in_estate,estates


def agent_menu():
    print("Which of the following functions would you like to perform our dear agent:")
    print("1)Adding a house")
    print("2)Add a new estate")
    print("3)See my estates")
    print("4)See clients in an estate")
    print("5)Remove a house")
    print("6)Remove an estate")
    print("7)Go back to the main page to change user")
    print("8)Exit the application")

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
            print("Enter estate id ")
            d=input(">")
            search_for_clients_in_estate(d)

        elif choice=="5":
            print("Enter id of house you want to demolish")
            z=input(">")
            remove_a_house(z)

        elif choice=="6":
            print("Enter id of estate you would like to remove")
            m=input(">")
            remove_an_estate(m)

        elif choice=="7":
            main_menu()

        elif choice=="8":
            print("Thank you for using our system")
            exit()

        else:
            print("Invalid choice entered")


def client_menu():
    print("1)See houses that are available")
    print("2)Buy a house")
    print("3)Go back to the main menu to change user")
    print("4)Exit application")
    
    

        

def client():
    while True:
        print("Welcome our prestigious client.Which of the following functions would you like to perform")
        client_menu()
        choice=input(">")
        if choice=="1":
            print("The following houses have no owners")
            see_available_houses()

        elif choice=="2":
            print("Enter your name")
            c=input(">")
            print("Enter location of the house")
            d=input(">")
            buy_a_house(c,d)
            print("House has been bought details for payment will be communicated to you later")
           
        elif choice=="3":
            main_menu()

        elif choice=="4":
            print("Thank you for using our system")
            exit()

        else:
            print("Invalid choice entered")

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