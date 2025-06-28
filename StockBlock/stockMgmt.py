from datetime import datetime
from sqlalchemy import text
from Utilities.util import getAlldata,postData
from requestModel.StockRequest import StockUniqueList,ProductUsingSerial

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
        print(request.expired)
        format_string = "%Y-%m-%d %H:%M:%S"
        expDate= datetime.strptime(str(request.expired),format_string) 
        createdDate = datetime.strptime(str(request.createdDate),format_string)
        diff_days:int = (expDate-createdDate).days
        print(diff_days)
        query = '''
        INSERT INTO stocks ("productName","subProduct","Qty","Price","gross","createdDate","inStock","outStock","totalStock","createdBy","expired","noofDays","barcode")
        VALUES('{pname}','{sub}',{qty},{price},{gross},DATE '{cdate}',{instock},{outstock},{totalstock},'{updatedby}',DATE '{exp}',{nod},{barcode});
        '''.format(pname = request.productName, sub=request.subProduct, qty = request.Qty, price=request.Price,
                   gross=request.gross, cdate=request.createdDate, instock=request.inStock, outstock=request.outStock,
                    totalstock=request.totalStock, updatedby=request.createdBy, exp=request.expired, nod=diff_days, barcode=request.barcode)
        print(text(query))
        data = postData(query)
        return {"data":data}
    
    def __getStockDetails(self,pid,stk,clmName)->int:
        return int(getAlldata(f'''select "{clmName}" from stocks where barcode={pid}''')[0][0]) + int(stk)

    def updateStock(self,request):
        print("Entering into the updateStock")
        pid = int(request.barcode)
        fetchQry = f'''
        select count("barcode") from stocks where barcode={pid}
        '''
        if getAlldata(fetchQry)[0][0] > 0:
            instockData = self.__getStockDetails(pid,request.inStock,"inStock")
            updateQry = '''
            update stocks set "productName"='{pname}',"subProduct"='{sub}',"Qty"={qty},"Price"={price},"gross"={gross},"createdDate"=DATE'{cdate}',"inStock"={instock},
            "createdBy"='{updatedby}' where "barcode" = {barcode}
            '''.format(pname=request.productName,sub=request.subProduct, qty = request.Qty, price=request.Price,
                   gross=request.gross, cdate=request.createdDate,instock=instockData,
                    totalstock=request.totalStock, updatedby=request.createdBy,barcode = request.barcode)
            print(updateQry)
            data = postData(updateQry)
            return {"data":data}
        else:
            print("Error: Could not find the product under the Barcode")
            return {"data":None}    
    
    def deleteProduct(self,barcode):
        print("Entering into the Delete function")
        deleteQry = f'''DELETE FROM stocks where barcode={barcode}'''
        data = postData(deleteQry)
        return {"data":data}
    
    def getProductUsingBarcode(self,barcode):
        print("Entering the function to get the product using Barcode")
        prQuery = f'''
        select "id","barcode","productName","subProduct" from stocks where barcode={barcode} 
        '''
        data = [ProductUsingSerial(id=x[0],barcode=x[1], productName=x[2], subProduct=x[3]) for x in getAlldata(prQuery)]
        print(data)
        return {"product":data}
    




