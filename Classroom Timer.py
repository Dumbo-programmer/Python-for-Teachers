import time
import os

def play_alarm_sound():
    # Depending on the operating system, this function might need adjustments
    # This plays a simple beep sound on most systems
    for _ in range(3):
        print("\a")
        time.sleep(1)

def log_timer(activity, duration):
    with open('timer_log.txt', 'a') as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {activity}: {duration} minutes\n")

def classroom_timer():
    print("Welcome to the Enhanced Classroom Timer!")
    timers = []

    while True:
        action = input("Enter 'set' to set a timer, 'start' to start timers, 'view' to view logs, or 'quit' to exit: ").lower()

        if action == 'set':
            activity = input("Enter the activity name: ")
            minutes = int(input("Enter the number of minutes: "))
            timers.append((activity, minutes))
        elif action == 'start':
            if not timers:
                print("No timers set.")
                continue

            for activity, minutes in timers:
                print(f"Starting timer for '{activity}' - {minutes} minute(s)")
                total_seconds = minutes * 60
                for remaining in range(total_seconds, 0, -1):
                    mins, secs = divmod(remaining, 60)
                    time_format = f"{mins:02d}:{secs:02d}"
                    print(f"Time remaining for {activity}: {time_format}", end='\r')
                    time.sleep(1)
                print(f"\nTime's up for {activity}!")
                play_alarm_sound()
                log_timer(activity, minutes)
            timers.clear()
        elif action == 'view':
            if os.path.exists('timer_log.txt'):
                with open('timer_log.txt', 'r') as file:
                    logs = file.read()
                    print("Timer Logs:\n", logs)
            else:
                print("No logs found.")
        elif action == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please enter 'set', 'start', 'view', or 'quit'.")

if __name__ == "__main__":
    classroom_timer()
