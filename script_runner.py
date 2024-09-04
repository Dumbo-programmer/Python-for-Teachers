import os
import subprocess

scripts = {
    "1": ("Gradebook Manager", "gradebook_manager.py"),
    "2": ("Attendance Tracker", "attendance_tracker.py"),
    "3": ("Lesson Plan Organizer", "lesson_plan_organizer.py"),
    "4": ("Quiz Generator", "quiz_generator.py"),
    "5": ("Assignment Reminder", "assignment_reminder.py"),
    "6": ("Student Report Card Generator", "report_card_generator.py"),
    "7": ("Seating Arrangement Planner", "seating_arrangement_planner.py"),
    "8": ("Classroom Timer", "classroom_timer.py"),
    "9": ("Student Feedback Form", "student_feedback_form.py"),
    "10": ("Classroom Poll", "classroom_poll.py"),
    "11": ("Lesson Timer with Breaks", "lesson_timer_with_breaks.py"),
    "12": ("Class Average Calculator", "class_average_calculator.py"),
    "13": ("Classroom Presentation Timer", "classroom_presentation_timer.py"),
    "14": ("Homework Checker", "homework_checker.py"),
    "15": ("Classroom Group Generator", "classroom_group_generator.py"),
    "16": ("Classroom Name Randomizer", "classroom_name_randomizer.py"),
    "17": ("Classroom Seating Chart Generator", "classroom_seating_chart_generator.py"),
    "18": ("Student Progress Tracker", "student_progress_tracker.py"),
    "19": ("Teacher's Gradebook", "teachers_gradebook.py"),
    "20": ("Student Report Generator", "student_report_generator.py")
}

def list_scripts():
    print("\nAvailable Scripts:")
    for key, (description, _) in scripts.items():
        print(f"{key}. {description}")

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except Exception as e:
        print(f"Error running {script_name}: {e}")

def main():
    while True:
        list_scripts()
        choice = input("\nEnter the number of the script to run (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        elif choice in scripts:
            _, script_name = scripts[choice]
            if os.path.exists(script_name):
                run_script(script_name)
            else:
                print(f"Script {script_name} not found.")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
