#Student Report Card Generator
import csv

def generate_report_card(student_name):
    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        grades = [row for row in reader if row[0] == student_name]

    if not grades:
        print("No grades found for the student.")
        return

    total_grade = sum(float(grade[2]) for grade in grades)
    average_grade = total_grade / len(grades)

    print(f"Report Card for {student_name}")
    for grade in grades:
        print(f"{grade[1]}: {grade[2]}")
    print(f"Average Grade: {average_grade:.2f}")

def report_card_generator():
    print("Welcome to the Student Report Card Generator!")
    student_name = input("Enter student name: ")
    generate_report_card(student_name)

if __name__ == "__main__":
    report_card_generator()
