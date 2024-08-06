#Lesson Timer with Breaks
import time

def lesson_timer_with_breaks():
    print("Welcome to the Lesson Timer with Breaks!")
    lesson_minutes = int(input("Enter the number of lesson minutes: "))
    break_minutes = int(input("Enter the number of break minutes: "))

    for i in range(lesson_minutes, 0, -1):
        print(f"Lesson time remaining: {i} minute(s)")
        time.sleep(60)
    print("Lesson time's up! Break time.")

    for i in range(break_minutes, 0, -1):
        print(f"Break time remaining: {i} minute(s)")
        time.sleep(60)
    print("Break time's up!")

if __name__ == "__main__":
    lesson_timer_with_breaks()
