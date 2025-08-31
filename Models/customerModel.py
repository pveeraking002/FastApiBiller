from sqlalchemy import Column,Integer,Text,String
from  sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class CustomerModel(Base):

    __tablename__='customers'

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    cname = Column(String)
    mobile = Column(String, unique=True)
    email = Column(String, unique=True)
    address=Column(Text)
    company = Column(String)



#insert into customers ("cname","mobile","email","address","company") values ('veera','9688994268','p.veeraking002@hotmail.com','14 test street', 'nil');