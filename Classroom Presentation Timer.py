#Classroom Presentation Timer
import time

def classroom_presentation_timer():
    print("Welcome to the Classroom Presentation Timer!")
    presentation_minutes = int(input("Enter the number of minutes for the presentation: "))
    warning_minutes = int(input("Enter the number of minutes for the warning: "))

    for i in range(presentation_minutes, 0, -1):
        if i == warning_minutes:
            print(f"Warning: Only {warning_minutes} minute(s) left!")
        print(f"Time remaining: {i} minute(s)")
        time.sleep(60)
    print("Time's up!")

if __name__ == "__main__":
    classroom_presentation_timer()
