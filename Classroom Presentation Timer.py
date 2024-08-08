import time
import csv
import os

def save_presentation_log(presentation_name, total_time, warning_times):
    filename = "presentation_log.csv"
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([presentation_name, total_time, ', '.join(map(str, warning_times))])
    print(f"Presentation log saved to {filename}")

def classroom_presentation_timer():
    print("Welcome to the Classroom Presentation Timer!")
    
    presentation_name = input("Enter the name of the presentation: ")
    presentation_minutes = int(input("Enter the number of minutes for the presentation: "))
    warning_times = input("Enter warning times in minutes (comma-separated): ").split(',')
    warning_times = [int(w.strip()) for w in warning_times if w.strip().isdigit()]
    
    total_seconds = presentation_minutes * 60
    warning_seconds = [w * 60 for w in warning_times]
    
    paused = False
    remaining_time = total_seconds
    
    while remaining_time > 0:
        minutes, seconds = divmod(remaining_time, 60)
        print(f"Time remaining: {minutes} minute(s) and {seconds} second(s)")
        
        if remaining_time in warning_seconds:
            warning_index = warning_seconds.index(remaining_time)
            print(f"Warning: Only {warning_times[warning_index]} minute(s) left!")
            os.system('say "Warning: Time is running out"')  # macOS text-to-speech
        
        time.sleep(1)
        remaining_time -= 1

        if remaining_time % 60 == 0:
            user_input = input("Press Enter to continue or type 'pause' to pause the timer: ").strip().lower()
            if user_input == "pause":
                paused = True
                while paused:
                    user_input = input("Timer is paused. Press Enter to resume: ").strip().lower()
                    if user_input == "":
                        paused = False

    print("Time's up!")
    os.system('say "Time is up"')  # macOS text-to-speech
    
    # Log the presentation timing
    save_presentation_log(presentation_name, presentation_minutes, warning_times)

if __name__ == "__main__":
    classroom_presentation_timer()
