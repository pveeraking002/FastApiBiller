from pydantic import BaseModel
class CustomerData(BaseModel):
    cname:str   | None
    email:str   | None
    address:str | None
    company:str | None
    mobile:str  | None

