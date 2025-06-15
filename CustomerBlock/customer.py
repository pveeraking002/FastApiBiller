from sqlalchemy import text
from requestModel.customerRequest import CustomerData
from Utilities.util import getAlldata,postData,deleteData
class Customer:
    _instance = None
    dbpool = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Customer,cls).__new__(cls)
        return cls._instance

    def __init__(self):
        print("customerBlock")

    def getCustomers(self):
        query = '''select * from "customers";'''
        data = getAlldata(query)
        #, mobile=x[2], email=x[3], address=x[4], company=x[5]
        cusData = [CustomerData(id=x[0], cname=x[1],mobile=x[2], email=x[3], address=x[4], company=x[5]) for x in data]
        return {"customers":cusData}
    
    #The Show - Jake Daniels (LYRICS)

    def addCustomer(self,request):
        print("inside the addCustomer Block")
        print(request.cname)
        query = '''
        INSERT INTO "customers" (id,"cname","mobile","email","address","company")
        VALUES({id},'{cname}','{mobile}','{email}','{address}','{company}')
        '''.format(id=request.id, cname=request.cname, mobile=request.mobile, email=request.email, address=request.address, company=request.company)
        data = postData(query)
        return {"data":data}
    
    def updateCustomer(self,request):
        return {"data": request}

    def deleteCustomer(self, cusId):
        print("Inside the deleteCustomer Function")
        print(cusId)
        query = '''DELETE FROM "customers" where id={id}'''.format(id=cusId)
        response = deleteData(query)
        return {"data":response}   
    
    def updateCustomer(self,request,cusId):
        print("inside the update customer Function")
        print(cusId)
        query = '''
        UPDATE "customers" SET "cname"='{cname}',"mobile"='{mobile}', 
        "email" ='{email}',"address"='{address}',"company"='{company}' WHERE 
        "id" = {id}
        '''.format(id=request.id, cname=request.cname, mobile=request.mobile, email=request.email, address=request.address, company=request.company)
        data = postData(query)
        return {"data":data}
    




