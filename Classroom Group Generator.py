import random

def classroom_group_generator():
    print("Welcome to the Classroom Group Generator!")
    
    # Input student names
    students_input = input("Enter student names separated by commas: ").strip()
    if not students_input:
        print("No students entered. Please provide a list of student names.")
        return

    students = [student.strip() for student in students_input.split(',')]
    
    # Input group size
    try:
        group_size = int(input("Enter the desired group size: ").strip())
        if group_size <= 0:
            print("Group size must be a positive integer.")
            return
    except ValueError:
        print("Invalid group size. Please enter a positive integer.")
        return

    # Shuffle students and create groups
    random.shuffle(students)
    groups = [students[i:i + group_size] for i in range(0, len(students), group_size)]
    
    # Handle leftovers
    if len(groups) > 1 and len(groups[-1]) < group_size:
        leftover_students = groups.pop()
    else:
        leftover_students = []

    # Output results
    print("\nGenerated Groups:")
    for i, group in enumerate(groups, start=1):
        print(f"Group {i}: {', '.join(group)}")
    
    if leftover_students:
        print(f"\nLeftover Students (not in a full group): {', '.join(leftover_students)}")

if __name__ == "__main__":
    classroom_group_generator()
