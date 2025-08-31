from requestModel.Transaction import TransactionRequestModel
from datetime import datetime


class TransactionsBlock:
    __instance=None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance=super(cls,TransactionsBlock).__new__(cls)
        return cls.__instance
    
    def getTransactions(self):
        pass 

    def postTransactions(self,request):
        try:
            print("Transaction Payload",request)
            format_string = "%d-%m-%Y"
            createdDate:datetime = datetime.strptime(request.createdDate,format_string)
            print("Created Date",createdDate)
            postQuery = '''
                INSERT INTO Transactions("createdDate","customerId","productName","qty","price","gross","discount","net","createdBy","company)
                VALUES({cd},{cid},'{pname}',{qty},{price},{gross},{discount},{net},'{cb}','{com}')  
            '''.format(cd = request.createdDate,cid = request.customerId, pname=request.productName, qty=request.qty,
                       price=request.price, gross=request.gross, discount=request.discount, net=request.net, 
                       cb=request.createdBy, com=request.company)
            print(postQuery)
            return {"Status":"Transactions is Posted"}
        except Exception as ex:
            print("We are getting erron in the posting the transactions",ex)
            return {"status":"Getting error in the transactions"}