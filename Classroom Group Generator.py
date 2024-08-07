#Classroom Group Generator
import random

def classroom_group_generator():
    print("Welcome to the Classroom Group Generator!")
    students = input("Enter student names separated by commas: ").split(',')
    group_size = int(input("Enter the desired group size: "))

    random.shuffle(students)
    groups = [students[i:i + group_size] for i in range(0, len(students), group_size)]

    print("Generated Groups:")
    for i, group in enumerate(groups, start=1):
        print(f"Group {i}: {', '.join(group)}")

if __name__ == "__main__":
    classroom_group_generator()

