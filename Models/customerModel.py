from sqlalchemy import Column,Integer,Text,String
from  sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CustomerModel(Base):

    __tablename__='customers'

    id = Column(Integer, primary_key=True, index=True)
    cname = Column(String)
    mobile = Column(String, unique=True)
    email = Column(String, unique=True)
    address=Column(Text)
    company = Column(String)


