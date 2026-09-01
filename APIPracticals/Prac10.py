from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt

app=FastAPI()

SECRET_KEY="mysecretkey"
ALGORITHM="HS256"

USERNAME="zahir"
PASSWORD="3216"

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    if (form_data.username==USERNAME and form_data.password==PASSWORD):
        token=jwt.encode({"sub":USERNAME},SECRET_KEY,algorithm=ALGORITHM)
        return {"access_token":token,"token_type":"bearer"}
    raise HTTPException(status_code=400,detail="wrong username or password")

@app.get("/profile")
def profile(token:str=Depends(oauth2_scheme)):
    data=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    return{"message":"profile accessed sucessfully",
           "username":data["sub"]}