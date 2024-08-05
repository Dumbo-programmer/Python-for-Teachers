import csv
from datetime import datetime

def attendance_tracker():
    print("Welcome to the Attendance Tracker!")
    date = datetime.now().strftime("%Y-%m-%d")
    attendance = {}

    while True:
        student_name = input("Enter student name (or 'done' to finish): ")
        if student_name.lower() == 'done':
            break
        status = input("Enter status (present/absent): ").lower()
        attendance[student_name] = status

    with open('attendance.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for student, status in attendance.items():
            writer.writerow([date, student, status])
    print("Attendance recorded successfully.")

if __name__ == "__main__":
    attendance_tracker()
