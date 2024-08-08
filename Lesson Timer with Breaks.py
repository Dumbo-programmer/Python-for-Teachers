import time

def countdown(minutes, label):
    for i in range(minutes, 0, -1):
        print(f"{label} time remaining: {i} minute(s) [{100 - (i / minutes) * 100:.2f}% complete]")
        time.sleep(60)

def lesson_timer_with_breaks():
    print("Welcome to the Lesson Timer with Breaks!")
    num_sessions = int(input("Enter the number of lesson/break cycles: "))

    for session in range(1, num_sessions + 1):
        print(f"\n--- Starting Session {session} ---")
        
        lesson_minutes = int(input(f"Enter the number of lesson minutes for Session {session}: "))
        break_minutes = int(input(f"Enter the number of break minutes for Session {session}: "))
        
        countdown(lesson_minutes, "Lesson")
        print("Lesson time's up! Break time.")
        
        skip_break = input("Do you want to skip the break? (yes/no): ").strip().lower()
        if skip_break != 'yes':
            countdown(break_minutes, "Break")
            print("Break time's up!")
        else:
            print("Break skipped.")
        
        if session < num_sessions:
            continue_session = input("Do you want to continue to the next session? (yes/no): ").strip().lower()
            if continue_session != 'yes':
                print("Timer stopped.")
                break
    print("All sessions complete!")

if __name__ == "__main__":
    lesson_timer_with_breaks()
