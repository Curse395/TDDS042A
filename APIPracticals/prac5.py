from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    postal_code: int=Field(min_length=1 , max_length=6)
    
class User(BaseModel):
    name: str
    age: int
    address: Address=Field(min_length=1,max_length=60)

@app.post("/users/")
async def create_user(user: User):
    return {
        "message": "User created",
        "user": user,
    }