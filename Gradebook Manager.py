import csv
import os

def add_grade():
    student_name = input("Enter student name: ")
    assignment = input("Enter assignment name: ")
    grade = input("Enter grade: ")

    with open('grades.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([student_name, assignment, grade])
    print("Grade added successfully.")

def view_grades():
    student_name = input("Enter student name (or press Enter to view all): ")
    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        found = False
        for row in reader:
            if student_name == "" or row[0].lower() == student_name.lower():
                print(f"{row[0]} - {row[1]}: {row[2]}")
                found = True
        if not found:
            print("No grades found for the student.")

def edit_grade():
    student_name = input("Enter student name: ")
    assignment = input("Enter assignment name: ")
    new_grade = input("Enter new grade: ")

    updated = False
    grades = []
    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0].lower() == student_name.lower() and row[1].lower() == assignment.lower():
                grades.append([student_name, assignment, new_grade])
                updated = True
            else:
                grades.append(row)

    if updated:
        with open('grades.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(grades)
        print("Grade updated successfully.")
    else:
        print("Grade not found.")

def delete_grade():
    student_name = input("Enter student name: ")
    assignment = input("Enter assignment name: ")

    grades = []
    deleted = False
    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not (row[0].lower() == student_name.lower() and row[1].lower() == assignment.lower()):
                grades.append(row)
            else:
                deleted = True

    if deleted:
        with open('grades.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(grades)
        print("Grade deleted successfully.")
    else:
        print("Grade not found.")

def calculate_average():
    student_name = input("Enter student name: ")
    total = 0
    count = 0

    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0].lower() == student_name.lower():
                total += float(row[2])
                count += 1

    if count > 0:
        average = total / count
        print(f"Average grade for {student_name}: {average:.2f}")
    else:
        print("No grades found for the student.")

def gradebook_manager():
    if not os.path.exists('grades.csv'):
        open('grades.csv', 'w').close()

    while True:
        print("\nWelcome to the Gradebook Manager!")
        choice =
