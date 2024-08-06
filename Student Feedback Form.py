#Student Feedback Form
import json

def student_feedback_form():
    print("Welcome to the Student Feedback Form!")
    feedback = []

    while True:
        student_name = input("Enter student name (or 'done' to finish): ")
        if student_name.lower() == 'done':
            break
        comments = input("Enter feedback comments: ")
        feedback.append({"student_name": student_name, "comments": comments})

    with open('feedback.json', 'w') as jsonfile:
        json.dump(feedback, jsonfile, indent=4)
    print("Feedback saved successfully.")

if __name__ == "__main__":
    student_feedback_form()
