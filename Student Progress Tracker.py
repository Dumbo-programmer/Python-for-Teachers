#Student Progress Tracker
import csv

def student_progress_tracker():
    print("Welcome to the Student Progress Tracker!")
    student_name = input("Enter student name: ")

    total_grade = 0
    count = 0

    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == student_name:
                total_grade += float(row[2])
                count += 1

    if count == 0:
        print("No grades found for the student.")
        return

    average_grade = total_grade / count
    print(f"Average Grade for {student_name}: {average_grade:.2f}")

if __name__ == "__main__":
    student_progress_tracker()
