import json
from datetime import datetime

LESSON_PLAN_FILE = 'lesson_plans.json'

def load_lesson_plans():
    """Load lesson plans from the JSON file."""
    try:
        with open(LESSON_PLAN_FILE, 'r') as jsonfile:
            return [json.loads(line) for line in jsonfile]
    except FileNotFoundError:
        return []

def save_lesson_plans(lesson_plans):
    """Save lesson plans to the JSON file."""
    with open(LESSON_PLAN_FILE, 'w') as jsonfile:
        for plan in lesson_plans:
            json.dump(plan, jsonfile)
            jsonfile.write('\n')

def add_lesson_plan(lesson_plans):
    """Add a new lesson plan."""
    date = input("Enter the date (YYYY-MM-DD): ")
    topic = input("Enter the lesson topic: ")
    objectives = input("Enter the lesson objectives: ")
    activities = input("Enter the lesson activities: ")

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    lesson_plan = {
        "date": date,
        "topic": topic,
        "objectives": objectives,
        "activities": activities
    }

    lesson_plans.append(lesson_plan)
    save_lesson_plans(lesson_plans)
    print("Lesson plan saved successfully.")

def view_lesson_plans(lesson_plans):
    """View all lesson plans."""
    if not lesson_plans:
        print("No lesson plans found.")
        return

    for i, plan in enumerate(lesson_plans, start=1):
        print(f"\nLesson Plan {i}")
        print(f"Date: {plan['date']}")
        print(f"Topic: {plan['topic']}")
        print(f"Objectives: {plan['objectives']}")
        print(f"Activities: {plan['activities']}")

def search_lesson_plans(lesson_plans):
    """Search for lesson plans by date or topic."""
    search_term = input("Enter date (YYYY-MM-DD) or topic to search: ").strip().lower()
    found_plans = [plan for plan in lesson_plans if search_term in plan['date'].lower() or search_term in plan['topic'].lower()]

    if found_plans:
        for plan in found_plans:
            print(f"\nDate: {plan['date']}")
            print(f"Topic: {plan['topic']}")
            print(f"Objectives: {plan['objectives']}")
            print(f"Activities: {plan['activities']}")
    else:
        print("No lesson plans found matching the search criteria.")

def delete_lesson_plan(lesson_plans):
    """Delete a lesson plan."""
    date = input("Enter the date of the lesson plan to delete (YYYY-MM-DD): ").strip()

    filtered_plans = [plan for plan in lesson_plans if plan['date'] != date]

    if len(filtered_plans) == len(lesson_plans):
        print("No lesson plan found with that date.")
    else:
        save_lesson_plans(filtered_plans)
        print("Lesson plan deleted successfully.")

def lesson_plan_organizer():
    lesson_plans = load_lesson_plans()

    print("Welcome to the Lesson Plan Organizer!")
    while True:
        print("\nOptions:")
        print("1. Add a new lesson plan")
        print("2. View all lesson plans")
        print("3. Search for a lesson plan")
        print("4. Delete a lesson plan")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_lesson_plan(lesson_plans)
        elif choice == '2':
            view_lesson_plans(lesson_plans)
        elif choice == '3':
            search_lesson_plans(lesson_plans)
        elif choice == '4':
            delete_lesson_plan(lesson_plans)
        elif choice == '5':
            print("Exiting the Lesson Plan Organizer.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    lesson_plan_organizer()
