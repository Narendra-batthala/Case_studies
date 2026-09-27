from fastapi import FastAPI
import database
app=FastAPI()


@app.get("/")
def home():

    return {
        "message": "Ride Management System"
    }

@app.get("/rides")
def rides():
    return database.display_rides()

@app.post("/rides")
def add_ride(customer: str,driver: str,vehicle: str,source:str ,destination:str,distance: float,fare: float,status:str):
    return database.insert_ride(customer,driver,vehicle,source,destination,distance,fare,status)


@app.put("/rides{id}")
def update_ride(id:int ,customer: str,driver: str,vehicle: str,source:str ,destination:str,distance: float,fare: float,status:str):
    return database.update_ride(id, customer, driver, vehicle,
            source, destination, distance, fare, status)

@app.delete("/sales{id}")
def delete_ride(id:int):
    return database.delete_ride(id)