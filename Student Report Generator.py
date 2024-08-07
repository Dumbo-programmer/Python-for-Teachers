# Student Report Generator
import csv

def generate_student_report(student_name):
    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        grades = [row for row in reader if row[0] == student_name]

    if not grades:
        print("No grades found for the student.")
        return

    total_grade = sum(float(grade[2]) for grade in grades)
    average_grade = total_grade / len(grades)

    print(f"Report for {student_name}")
    for grade in grades:
        print(f"{grade[1]}: {grade[2]}")
    print(f"Average Grade: {average_grade:.2f}")

def student_report_generator():
    print("Welcome to the Student Report Generator!")
    student_name = input("Enter student name: ")
    generate_student_report(student_name)

if __name__ == "__main__":
    student_report_generator()
