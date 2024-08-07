#Classroom Name Randomizer
import random

def classroom_name_randomizer():
    print("Welcome to the Classroom Name Randomizer!")
    students = input("Enter student names separated by commas: ").split(',')

    selected_student = random.choice(students)
    print(f"Selected student: {selected_student}")

if __name__ == "__main__":
    classroom_name_randomizer()
