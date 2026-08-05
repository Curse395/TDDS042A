import time

def verify_student():
    print("Verifying student...")
    time.sleep(2)  
    print("Student verified successfully.")
    
def fetch_attendance():
    print("Fetching attendance...")
    time.sleep(3) 
    print("Attendance Loaded\n")
    
def fetch_marks():
    print("Fetching marks...")
    time.sleep(2)  
    print("Marks Loaded\n")
    
print("======== Student Portal ========\n")

start=time.time()

verify_student()
fetch_attendance()
fetch_marks()

end=time.time()

print(f"\nTotal Time={end-start:.2f} seconds")