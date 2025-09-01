from requestModel.Transaction import TransactionRequestModel,GetTransactionBody
from datetime import datetime
from Utilities.util import getAlldata,postData
from requestModel.customerRequest import CustomerData
from CustomerBlock.customer import Customer


class TransactionsBlock:
    __instance=None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance=super(cls,TransactionsBlock).__new__(cls)
        return cls.__instance

    #public access points     
    def getTransactions(self):
        return self.__BackgroundGetTransactions()

    def postTransactions(self,request):
        return self.__BackgroundPostTransactions(request=request) 


    #background tasks 
    def __BackgroundGetTransactions(self):
        getAllTransactionQuery = '''
            select * from "transactions";
        ''' 
        data = [GetTransactionBody(createdDate=str(dt[1]),
                                   customerId=str(dt[2]),
                                   productName=str(dt[3]),
                                   qty=str(dt[4]),
                                   customer = Customer().getCustomersById(dt[2]))for dt in getAlldata(getAllTransactionQuery)]     
        
        #print(data)
        return {"result":data} 

    def __BackgroundPostTransactions(self,request):
        try:
            print("Transaction Payload",request)
            format_string = "%Y-%m-%d"
            createdDate:datetime = datetime.strptime(request.createdDate,format_string)
            print("Created Date",createdDate)
            postQuery = '''
                INSERT INTO "transactions" ("createdDate","customerId","productName","qty","price","gross","discount","net","createdBy","company")
                VALUES('{cd}',{cid},'{pname}',{qty},{price},{gross},{discount},{net},'{cb}','{com}')  
            '''.format(cd = request.createdDate,cid = request.customerId, pname=request.productName, qty=request.qty,
                    price=request.price, gross=request.gross, discount=request.discount, net=request.net, 
                    cb=request.createdBy, com=request.company)
            print(postQuery)
            postStatus = postData(postQuery)
            return {"Status":"Transactions is Posted", "data":request, "postStatus":postStatus}
        except Exception as ex:
            print("We are getting erron in the posting the transactions",ex)
            return {"status":"Getting error in the transactions"}

