d={}


def display_rides():
    if d=={}:
        return "No Data"
    else:
        return d



def insert_ride(customer,driver,vehicle,source,destination,distance,fare,status):

    if d=={}:
        id=101
    else:
        id=max(d.keys())+1
    d[id]={
        "customer":customer,
        "driver": driver,
        "vehicle": vehicle,
        "source": source,
        "destination": destination,
        "distance":distance,
        "fare": fare,
        "status": status
    }
    return "Sucessfully added"


def update_ride(Id,customer,driver,vehicle,source,destination,distance,fare,status):
    if Id in d.keys():
        d[Id]={
            
                "customer":customer,
                "driver": driver,
                "vehicle": vehicle,
                "source": source,
                "destination": destination,
                "distance":distance,
                "fare": fare,
                "status": status
            }
        return "Sucessfully Updated"
    else:
        return "Id not found"

def delete_ride(Id):
    if Id in d:
        del d[Id]
        new_d = {}

        for i, ride in enumerate(d.values(), start=101):
            new_d[i] = ride

        d.clear()
        d.update(new_d)
        return "sucessfully deleted"
    else:
        return "ID Not Found"
    



     






     