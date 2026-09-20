
from fastapi import FastAPI
import database

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Sales Management API"
    }


# Get all sales
@app.get("/sales")
def get_sales():

    return database.sales_details()


# Search sale by ID and name
@app.get("/sales/{ID}/{name}")
def search_sale(ID: int, name: str):

    sale = database.get_person(ID, name)

    if sale:

        return sale

    return {
        "message": "Sale not found!"
    }


# Add a new sale
@app.post("/sales")
def add_sale(name: str, product: str, quantity: int, price: float, region: str):

    database.insert_sale(name,product,quantity,price,region)

    return {
        "message": "Sale added successfully!"
    }


# Update a sale
@app.put("/sales/{sale_id}")
def update_sale(sale_id: int,name: str,product: str,quantity: int,price: float,region: str):

    result = database.update_sale(sale_id,name,product,quantity,price,region)

    if result:

        return {
            "message": "Sale updated successfully!"
        }

    return {
        "message": "Sale ID not found!"
    }


# Delete a sale
@app.delete("/sales/{sale_id}")
def delete_sale(sale_id: int):

    result = database.delete_sale(sale_id)

    if result:

        return {
            "message": "Sale deleted successfully!"
        }

    return {
        "message": "Sale ID not found!"
    }