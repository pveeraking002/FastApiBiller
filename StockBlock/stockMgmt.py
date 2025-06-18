from sqlalchemy import text
from Utilities.util import getAlldata,postData
from requestModel.StockRequest import StockUniqueList

class StockManagement:
    _stkInstance = None
    
    def __new__(cls):
        if cls._stkInstance == None:
            cls._stkInstance = super(cls,StockManagement).__new__(cls)
        return cls._stkInstance
    
    def getUniqueStocks(self):
        print("Entering into the getUniqueStocks Functions")
        query = '''SELECT DISTINCT "productName" FROM "stocks" '''
        subProduct = '''
        select Distinct "subProduct", "productName" from stocks where "productName" in 
        (SELECT DISTINCT "productName" FROM "stocks");
        '''
        print(getAlldata(subProduct))
        data = [StockUniqueList(productName=dt[0],subProduct=[sub[0] for sub in getAlldata(subProduct) if sub[1] == dt[0]]) 
                for dt in getAlldata(query)]
        print("data",data)
        return {"data":data}

    def insertStock(self,request):
        print("Entering into Inserting prodcct")
        query = '''
        INSERT INTO stocks ("productName","subProduct","Qty","Price","gross","createdDate","inStock","outStock","totalStock","createdBy","expired","noofDays")
        VALUES('{pname}','{sub}',{qty},{price},{gross},DATE '{cdate}',{instock},{outstock},{totalstock},'{updatedby}',DATE '{exp}',{nod});
        '''.format(pname = request.productName, sub=request.subProduct, qty = request.Qty, price=request.Price,
                   gross=request.gross, cdate=request.createdDate, instock=request.inStock, outstock=request.outStock,
                    totalstock=request.totalStock, updatedby=request.createdBy, exp=request.expired, nod= request.noofDays)
        print(text(query))
        data = postData(query)
        return {"data":data}
    




    