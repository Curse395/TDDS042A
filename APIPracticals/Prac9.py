from fastapi import FastAPI , Depends

app = FastAPI()

def Check_user():
    print ("1 checking if user exists")
    return "User exists"

@app.get("/check_user")
def dependent_api(user=Depends(Check_user)):
    print("2 running the endpoint")
    print("3 endpoint is returning the response")
    return {"user": user} 