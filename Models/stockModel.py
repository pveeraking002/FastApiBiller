from sqlalchemy import Column,Integer,Text,String,Float,DateTime
from datetime import datetime
from  sqlalchemy.ext.declarative import declarative_base

StockBase = declarative_base()

class StockModel(StockBase):
    __tablename__= "stocks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    productName = Column(String)
    subProduct = Column(String)
    Qty = Column(Integer)
    Price = Column(Float)
    gross = Column(Float)
    createdDate = Column(DateTime)
    inStock = Column(String)
    outStock = Column(String)
    totalStock = Column(String)
    createdBy = Column(String)
    expired = Column(DateTime)
    noofDays = Column(Integer)

'''
INSERT INTO stocks ("productName","subProduct","Qty","Price","gross","createdDate","inStock","outStock","totalStock","createdBy","expired","noofDays") VALUES('product1','AC',4,20.00,20.00,'20/05/1991',10,2,12,'veera','20/05/1991',20);

NSERT INTO stocks (productName,subProduct,Qty,Price,gross,createdDate,inStock,outStock,totalStock,createdBy,expired,noofDays) VALUES('product1','AC',4,20.00,20.00,'20/05/1991',10,2,12,'veera','20/05/1991',20);

INSERT INTO stocks ("productName","subProduct","Qty","Price","gross","createdDate","inStock","outStock","totalStock","createdBy","expired","noofDays") VALUES('product1','AC',4,20.00,20.00,DATE '2015-05-16',10,2,12,'veera',DATE '2015-05-16',20);
'''
