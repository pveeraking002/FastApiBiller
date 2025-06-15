import sqlalchemy
from sqlalchemy.orm import sessionmaker

def create_db_pool():
    pool = None
    try:
        if pool == None:
            print("Enter into the pool function",pool)
            DB_URL = "postgresql://postgres:postgres@db:5432/biller"
            pool = sqlalchemy.create_engine(DB_URL)
            #sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=pool)
            print("pool Created")
        return pool 
    except Exception as exp:
        print("Found issues on DbConnection",exp)


