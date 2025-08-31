from sqlalchemy import Column,Integer,Text,String,Float,DateTime,ForeignKey
from datetime import datetime
from  sqlalchemy.ext.declarative import declarative_base
from Models.customerModel import CustomerModel

TransactionsBase = declarative_base()

class Transactions(TransactionsBase):
    __tablename__ = "transactions"

    id  = Column(Integer, primary_key=True, index=True, autoincrement=True)
    createdDate = Column(DateTime)
    customerId = Column(Integer)
    productName=Column(Text)
    qty = Column(Integer)
    price = Column(Float)
    gross = Column(Float)
    discount=Column(Float)
    net=Column(Float)
    createdBy=Column(Text)
    company = Column(Text)





