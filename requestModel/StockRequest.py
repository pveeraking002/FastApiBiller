from pydantic import BaseModel 
from datetime import datetime

class StockUniqueList(BaseModel):
    productName:str | None 
    subProduct:list


class ProductsRequestModel(BaseModel):
    productName:str
    subProduct:str
    Qty:int
    Price:float
    gross:float
    createdDate:datetime
    inStock:int
    outStock:int
    totalStock:int
    createdBy:str
    expired:datetime
    #noofDays:int
    barcode:int


