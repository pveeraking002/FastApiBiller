import os 
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_DI",None)
CLIENT_SECRET=os.environ.get("CLIENT_SECRET",None)


#Database Connection
CONNECT_DB_URL = os.environ.get("DB_URL",None)


