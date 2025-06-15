from sqlalchemy import text
from Connector.connector import create_db_pool

def getAlldata(query)-> any:
    try:
        pool = create_db_pool()
        with pool.connect() as conn:
            data = conn.execute(text(query)).fetchall()
            pool.dispose()
            return data  
    except Exception as exp:
        print("Error on getAllData Module",exp)

def postData(query)-> bool:
    try:
        pool = create_db_pool()
        with pool.connect() as conn:
            conn.execute(text(query))
            conn.commit()
        pool.dispose()
        return True
    except Exception as exp:
        print("Found error on Post Data",exp)
        return False

def deleteData(query):
    try:
        pool = create_db_pool()
        with pool.connect() as conn:
            conn.execute(text(query))
            conn.commit()
        pool.dispose()
        return True 
    except Exception as exp:
        print("Error in Delete Function",exp)
        return False