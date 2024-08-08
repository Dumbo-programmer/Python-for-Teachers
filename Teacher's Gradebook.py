import csv
import os

def add_grade():
    student_name = input("Enter student name: ").strip()
    assignment = input("Enter assignment name: ").strip()
    while True:
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the grade.")
    
    with open('grades.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([student_name, assignment, grade])
    print("Grade added successfully.")

def view_grades():
    if not os.path.isfile('grades.csv'):
        print("No grades found. Please add some grades first.")
        return

    grades = []
    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            grades.append(row)
    
    if not grades:
        print("No grades available.")
        return
    
    print("\nGradebook:")
    for row in grades:
        print(f"{row[0]} - {row[1]}: {row[2]}")
    
    # Calculate and display summary statistics
    assignments = {}
    for student, assignment, grade in grades:
        grade = float(grade)
        if assignment not in assignments:
            assignments[assignment] = []
        assignments[assignment].append(grade)
    
    print("\nSummary Statistics:")
    for assignment, grades in assignments.items():
        avg_grade = sum(grades) / len(grades)
        highest_grade = max(grades)
        lowest_grade = min(grades)
        print(f"{assignment}:")
        print(f"  Average grade: {avg_grade:.2f}")
        print(f"  Highest grade: {highest_grade:.2f}")
        print(f"  Lowest grade: {lowest_grade:.2f}")

def teachers_gradebook():
    print("Welcome to the Teacher's Gradebook!")
    choice = input("Do you want to (1) add a grade or (2) view grades? Enter 1 or 2: ").strip()

    if choice == '1':
        add_grade()
    elif choice == '2':
        view_grades()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    teachers_gradebook()
