from fastapi import BackgroundTasks, FastAPI
import time

app = FastAPI()


def send_email(email: str):
    print(f"Sending email to {email}...")
    time.sleep(5)
    print(f"Email sent successfully to {email}!")

@app.post("/register")
async def register(email: str, background_tasks: BackgroundTasks):
    
    print("User registered successfully!")
    
    background_tasks.add_task(send_email, email)

    return {
        "message": "Registration Successful!",
        "status": "Email will be sent in the background.",
    }
