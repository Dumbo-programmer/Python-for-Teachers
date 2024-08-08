import random

def classroom_name_randomizer():
    print("Welcome to the Classroom Name Randomizer!")
    
    while True:
        students = input("Enter student names separated by commas (or type 'exit' to quit): ").strip()
        if students.lower() == 'exit':
            print("Goodbye!")
            break
        
        student_list = [student.strip() for student in students.split(',') if student.strip()]
        
        if not student_list:
            print("No valid student names entered. Please try again.")
            continue
        
        selected_student = random.choice(student_list)
        print(f"Selected student: {selected_student}")

if __name__ == "__main__":
    classroom_name_randomizer()
