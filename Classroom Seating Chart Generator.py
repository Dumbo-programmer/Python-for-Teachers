#Classroom Seating Chart Generator
import random

def classroom_seating_chart_generator():
    print("Welcome to the Classroom Seating Chart Generator!")
    students = input("Enter student names separated by commas: ").split(',')
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    if len(students) > rows * cols:
        print("Not enough seats for all students.")
        return

    random.shuffle(students)
    seating_chart = [[None for _ in range(cols)] for _ in range(rows)]

    i = 0
    for r in range(rows):
        for c in range(cols):
            if i < len(students):
                seating_chart[r][c] = students[i]
                i += 1

    print("Generated Seating Chart:")
    for r in range(rows):
        print(" | ".join([seat if seat else "Empty" for seat in seating_chart[r]]))

if __name__ == "__main__":
    classroom_seating_chart_generator()
