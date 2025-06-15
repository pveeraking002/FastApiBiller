from pydantic import BaseModel
class CustomerData(BaseModel):
    id:int
    cname:str   | None
    mobile:str  | None
    email:str   | None
    address:str | None
    company:str | None

