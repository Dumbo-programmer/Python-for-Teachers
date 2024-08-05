#Lesson Plan Organizer
import json

def lesson_plan_organizer():
    print("Welcome to the Lesson Plan Organizer!")
    date = input("Enter the date (YYYY-MM-DD): ")
    topic = input("Enter the lesson topic: ")
    objectives = input("Enter the lesson objectives: ")
    activities = input("Enter the lesson activities: ")

    lesson_plan = {
        "date": date,
        "topic": topic,
        "objectives": objectives,
        "activities": activities
    }

    with open('lesson_plans.json', 'a') as jsonfile:
        json.dump(lesson_plan, jsonfile)
        jsonfile.write('\n')
    print("Lesson plan saved successfully.")

if __name__ == "__main__":
    lesson_plan_organizer()
