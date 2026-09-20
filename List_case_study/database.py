sales=[]


def sales_details():
    return sales

sales_details()

def insert_sale(name, product, quantity, price, region):
    if sales==[]:
        new_id=101
    else:
        new_id = max(sale[0] for sale in sales) + 1
    new_sale = [new_id, name.capitalize(), product.capitalize(), quantity, price, region.capitalize()]

    sales.append(new_sale)
    return "Sucessfully added"


def get_person(ID,name):
    for i,sub in enumerate(sales):
        if ID in sub and name.capitalize() in sub:
            return (f'ID: {sub[0]} | Names:{sub[1]} | Products:{sub[2]} | Units:{sub[3]} | price:{sub[4]} | Region:{sub[5]}')
        
    return ("Not found check Id and name and Retry")



def update_sale(sale_id, name, product, quantity, price, region):
    for sale in sales:
        if sale[0] == sale_id:
            sale[1] = name.capitalize()
            sale[2] = product.capitalize()
            sale[3] = quantity
            sale[4] = price
            sale[5] = region.capitalize()
            
            return "\nSale updated successfully!\n"

    return "\nSale ID not found can't update\n"



def delete_sale(sale_id):
    for sale in sales:
            if sale[0] == sale_id:
                sales.remove(sale)
                for i, sub in enumerate(sales, start=101):
                    sub[0] = i
                return "\nSucessfully deleted\n"
    return "\nSale ID not found can't delete\n"




