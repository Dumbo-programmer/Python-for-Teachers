#Seating Arrangement Planner
import random

def seating_arrangement_planner():
    print("Welcome to the Seating Arrangement Planner!")
    students = input("Enter student names separated by commas: ").split(',')

    random.shuffle(students)
    print("Seating Arrangement:")
    for i, student in enumerate(students, start=1):
        print(f"Seat {i}: {student.strip()}")

if __name__ == "__main__":
    seating_arrangement_planner()
