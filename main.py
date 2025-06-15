from contextlib import asynccontextmanager
from fastapi import FastAPI,Request
from CustomerBlock.customer import Customer
from Connector.connector import create_db_pool
from Models.customerModel import Base
from requestModel.customerRequest import CustomerData 

db_pool = None

@asynccontextmanager 
async def Dbs(lifespan:FastAPI):
    while True:
        global db_pool
        db_pool = create_db_pool()
        Base.metadata.create_all(bind=db_pool)
        print("checking Connections")
        yield
        db_pool.dispose()
        print("connection Closed")


app = FastAPI(lifespan=Dbs)



@app.get("/")
def indexPage():
    return "hello World"


#customerBlock

@app.get("/getcustomers")
def getCustomers():
    json_data = Customer().getCustomers()
    return json_data

@app.post("/addcustomer")
def addCustomer(request:CustomerData):  
    print(request) 
    json_data = Customer().addCustomer(request)
    return json_data

@app.patch("/updatecustomer/{cusId}")
def addCustomer(cusId:int, request:CustomerData):
    json_data = Customer().updateCustomer(request,cusId)
    return json_data

@app.delete("/deletecustomer/{cusId}")
def deleteCustomer(cusId:int):
    json_data = Customer().deleteCustomer(cusId)
    return json_data


