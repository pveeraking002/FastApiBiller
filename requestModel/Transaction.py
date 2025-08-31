from pydantic import BaseModel
from datetime import datetime

class TransactionRequestModel(BaseModel):
    createdDate:str
    customerId:int #getting the customer form the customer Table 
    productName:str 
    qty:int
    price:float
    gross:float 
    discount:float
    net:float 
    createdBy:str | None 



