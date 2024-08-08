import csv
from collections import defaultdict

def read_grades(file_path):
    """Read grades from a CSV file and return them as a dictionary."""
    grades = defaultdict(list)
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 3:  # Ensure row has exactly 3 columns
                    student, assignment, grade = row
                    try:
                        grades[assignment].append(float(grade))
                    except ValueError:
                        print(f"Warning: Invalid grade '{grade}' for assignment '{assignment}' by student '{student}'. Skipping.")
    except FileNotFoundError:
        print("The grades file does not exist. Please add grades first.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return grades

def class_average_calculator():
    print("Welcome to the Class Average Calculator!")
    file_path = 'grades.csv'

    # Read grades from file
    grades = read_grades(file_path)

    if not grades:
        print("No grades data available to calculate average.")
        return

    assignment = input("Enter the assignment name (or 'list' to view all assignments): ").strip()

    if assignment.lower() == 'list':
        print("Available assignments:")
        for assign in grades.keys():
            print(f"- {assign}")
        return

    if assignment not in grades:
        print(f"No grades found for the assignment '{assignment}'.")
        return

    # Calculate average grade
    grades_list = grades[assignment]
    average_grade = sum(grades_list) / len(grades_list)
    print(f"Average Grade for '{assignment}': {average_grade:.2f}")

if __name__ == "__main__":
    class_average_calculator()
