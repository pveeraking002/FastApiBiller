from contextlib import asynccontextmanager
from fastapi import FastAPI,Request
from CustomerBlock.customer import Customer
from StockBlock.stockMgmt import StockManagement
from Connector.connector import create_db_pool
from Models.customerModel import Base
from Models.stockModel import StockBase
from requestModel.StockRequest import ProductsRequestModel, StockUniqueList
from requestModel.customerRequest import CustomerData 
from fastapi.middleware.cors import CORSMiddleware

db_pool = None

@asynccontextmanager 
async def Dbs(lifespan:FastAPI):
    while True:
        global db_pool
        db_pool = create_db_pool()
        Base.metadata.create_all(bind=db_pool)
        StockBase.metadata.create_all(bind=db_pool)
        print("checking Connections")
        yield
        db_pool.dispose()
        print("connection Closed")


app = FastAPI(lifespan=Dbs)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

#docker exec -it df50542db708 psql -U postgres -d postgres

#Stock api
@app.get("/productlist")
async def getUniqueProductList():
    json_data = StockManagement().getUniqueStocks()
    return json_data 

@app.post("/postproduct")
async def postProduct(request:ProductsRequestModel):
    json_data = StockManagement().insertStock(request)
    return json_data 

@app.patch("/updateproduct")
async def updateProduct(request:ProductsRequestModel):
    json_data = StockManagement().updateStock(request)
    return json_data

@app.delete("/deleteproduct/{barcode}")
async def deleteProduct(barcode:int):
    json_data = StockManagement().deleteProduct(barcode)
    return json_data

@app.get("/product/{barcode}")
async def getProductUsingBarcode(barcode:int):
    print("barcode",barcode)
    json_data = StockManagement().getProductUsingBarcode(barcode)
    return json_data
#End Stock api 
