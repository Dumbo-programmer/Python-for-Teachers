import random
import os

def seating_arrangement_planner():
    print("Welcome to the Seating Arrangement Planner!")

    # Input student names
    students_input = input("Enter student names separated by commas: ")
    students = [student.strip() for student in students_input.split(',') if student.strip()]
    
    if not students:
        print("No valid student names provided.")
        return
    
    # Shuffle students
    random.shuffle(students)

    # Print the seating arrangement
    print("\nSeating Arrangement:")
    for i, student in enumerate(students, start=1):
        print(f"Seat {i}: {student}")

    # Save the seating arrangement to a file
    save_choice = input("\nWould you like to save this arrangement to a file? (yes/no): ").strip().lower()
    if save_choice == 'yes':
        file_name = input("Enter the file name (without extension): ").strip() + '.txt'
        with open(file_name, 'w') as file:
            file.write("Seating Arrangement:\n")
            for i, student in enumerate(students, start=1):
                file.write(f"Seat {i}: {student}\n")
        print(f"Seating arrangement saved to '{file_name}'.")
    else:
        print("Seating arrangement not saved.")

if __name__ == "__main__":
    seating_arrangement_planner()
