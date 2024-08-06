#Classroom Timer
import time

def classroom_timer():
    print("Welcome to the Classroom Timer!")
    minutes = int(input("Enter the number of minutes: "))

    for i in range(minutes, 0, -1):
        print(f"Time remaining: {i} minute(s)")
        time.sleep(60)
    print("Time's up!")

if __name__ == "__main__":
    classroom_timer()
