import database


USER_CHOICE = """
Enter:

- 'a' to add a sale
- 'l' to list all sales
- 's' to search for a sales_person
- 'd' to delete a sale
- 'p' to update sale
- 'q' to quit

Your choice: """

#ADD SalesMan
def add_salesman():
    name = input("Enter person name: ")
    product = input("Enter product: ")
    units = int(input("Enter Units: "))
    price = float(input("Enter Price: "))
    region = input("Enter region: ")
    
    database.insert_sale(name,product,units,price,region)
# List of sales
def sales_list():
    sales=database.sales_details()
    if sales==[]:
            print("No data")
            return
    else:
        print("ID\tNames\tProducts\tUnits\tprice\tRegion")

        print(('-')*60)
        for i in range(len(sales)):
            print(sales[i][0], end='\t')
            print(sales[i][1], end='\t')
            print(sales[i][2], end='\t\t')
            print(sales[i][3], end='\t')
            print(sales[i][4], end='\t')
            print(sales[i][5], end='\t')
            print()
# Sepecific salesman details
def search_salesman():
    ID = int(input("Enter ID: "))
    name=input("Enter salesMan name: ")
    res=database.get_person(ID,name)
    print(res)

# delete salesman

def del_salesman():
    ID=int(input("Enter salesman ID: "))
    res=database.delete_sale(ID)
    print(res)

def update_salesman():
    Id=int(input("Enter id of the salesman to update"))
    name = input("Enter person name: ")
    product = input("Enter product: ")
    units = int(input("Enter Units: "))
    price = float(input("Enter Price: "))
    region = input("Enter region: ")
    res=database.update_sale(Id,name,product,units,price,region)
    print(res)

def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            add_salesman()
        elif user_input == "l":
            sales_list()
        elif user_input == "s":
            search_salesman()
        elif user_input == "d":
            del_salesman()
        elif user_input == "p":
            update_salesman()
        else:
            print("Invalid choice!")

        user_input = input(USER_CHOICE)

menu()
