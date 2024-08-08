import csv
from datetime import datetime
import os

def initialize_csv(file_path):
    """Create a new CSV file with headers if it does not exist."""
    if not os.path.isfile(file_path):
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'Student Name', 'Status'])
        print("Created a new attendance file with headers.")

def validate_status(status):
    """Validate that the status is either 'present' or 'absent'."""
    return status in ['present', 'absent']

def attendance_tracker():
    print("Welcome to the Attendance Tracker!")
    date = datetime.now().strftime("%Y-%m-%d")
    attendance = {}
    
    # Path to the CSV file
    file_path = 'attendance.csv'
    
    # Initialize CSV file with headers if needed
    initialize_csv(file_path)

    while True:
        student_name = input("Enter student name (or 'done' to finish): ").strip()
        if student_name.lower() == 'done':
            break
        if not student_name:
            print("Student name cannot be empty. Please try again.")
            continue
        status = input("Enter status (present/absent): ").strip().lower()
        if not validate_status(status):
            print("Invalid status. Please enter 'present' or 'absent'.")
            continue
        attendance[student_name] = status

    if not attendance:
        print("No attendance records to save.")
        return

    # Write attendance to the CSV file
    try:
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for student, status in attendance.items():
                writer.writerow([date, student, status])
        print("Attendance recorded successfully.")
    except Exception as e:
        print(f"An error occurred while saving the attendance: {e}")

    # Optional: Review recorded attendance
    review = input("Would you like to review the recorded attendance? (yes/no): ").strip().lower()
    if review == 'yes':
        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                print("\nAttendance Records:")
                for row in reader:
                    print(f"{row[0]} - {row[1]}: {row[2]}")
        except Exception as e:
            print(f"An error occurred while reading the attendance file: {e}")

if __name__ == "__main__":
    attendance_tracker()
