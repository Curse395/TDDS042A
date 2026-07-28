from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Address(BaseModel):
    street: str=Field(min_length=1,max_length=60)
    city: str
    postal_code: str=Field(min_length=1,max_length=6)
    
class User(BaseModel):
    name: str
    age: int=Field(gt=18,lt=60)
    address: Address

@app.post("/users/")
async def create_user(user: User):
    return {
        "message": "User created",
        "user": user,
    }