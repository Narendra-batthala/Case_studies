import database


USER_CHOICE = """
Enter:

- 'a' to add a ride
- 'l' to list of rides
- 'd' to delete a ride
- 'p' to update ride
- 'q' to quit

Your choice: """


def add_ride():
    customer = input("Enter Customer: ")
    driver = input("Enter Driver: ")
    vehicle = input("Enter Vehicle: ")
    source = input("Enter source ")
    destination = input("Enter destination: ")
    distance=int(input("Enter Distance: "))
    fare=int(input("Enter Fare: "))
    status=input("Enter Status: ")
    
    res=database.insert_ride(customer,driver,vehicle,source,destination,distance,fare,status)
    print(res)

def display_rides():
    rides=database.display_rides()
    if rides==[]:
            print("No data")
            return
    else:
        print(rides)

        

def get_update_input():
    Id = int(input("Enter Ride ID: "))
    customer = input("Enter customer: ")
    driver = input("Enter driver: ")
    vehicle = input("Enter vehicle: ")
    source = input("Enter source: ")
    destination = input("Enter destination: ")
    distance = float(input("Enter distance: "))
    fare = float(input("Enter fare: "))
    status = input("Enter status: ")

    res=database.update_ride(
        Id, customer, driver, vehicle,
        source, destination, distance, fare, status
    )
    print(res)

def delete_ride():
    id=int(input("Enter the ID to delete :"))
    res=database.delete_ride(id)
    print(res)

def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            add_ride()
        elif user_input == "l":
            display_rides()    
        elif user_input == "d":
            delete_ride()
        elif user_input == "p":
            get_update_input()
        else:
            print("Invalid choice!")

        user_input = input(USER_CHOICE)

menu()
