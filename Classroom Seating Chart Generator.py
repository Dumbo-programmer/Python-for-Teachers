import random
import json

def save_chart(seating_chart, filename):
    with open(filename, 'w') as file:
        json.dump(seating_chart, file)
    print(f"Seating chart saved to {filename}")

def load_chart(filename):
    try:
        with open(filename, 'r') as file:
            seating_chart = json.load(file)
            print(f"Seating chart loaded from {filename}")
            return seating_chart
    except FileNotFoundError:
        print(f"No seating chart found in {filename}")
        return None

def print_seating_chart(seating_chart):
    for row in seating_chart:
        print(" | ".join([seat if seat else "Empty" for seat in row]))
    print("\n")

def classroom_seating_chart_generator():
    print("Welcome to the Classroom Seating Chart Generator!")
    action = input("Do you want to (1) generate a new chart, (2) load an existing chart, or (3) quit? Enter 1, 2, or 3: ")

    if action == '1':
        students = input("Enter student names separated by commas: ").split(',')
        absentees = input("Enter names of absent students separated by commas (or leave blank if none): ").split(',')
        students = [student.strip() for student in students if student.strip() and student.strip() not in absentees]

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
        print_seating_chart(seating_chart)

        save_option = input("Do you want to save this seating chart? (yes/no): ").lower()
        if save_option == 'yes':
            filename = input("Enter the filename to save the seating chart (e.g., 'chart1.json'): ")
            save_chart(seating_chart, filename)

    elif action == '2':
        filename = input("Enter the filename to load the seating chart from (e.g., 'chart1.json'): ")
        seating_chart = load_chart(filename)
        if seating_chart:
            print("Loaded Seating Chart:")
            print_seating_chart(seating_chart)
    elif action == '3':
        print("Goodbye!")
        return
    else:
        print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    classroom_seating_chart_generator()
