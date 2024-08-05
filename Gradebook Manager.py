import csv

def gradebook_manager():
    print("Welcome to the Gradebook Manager!")
    choice = input("Do you want to (1) add a grade or (2) view grades? Enter 1 or 2: ")

    if choice == '1':
        student_name = input("Enter student name: ")
        assignment = input("Enter assignment name: ")
        grade = input("Enter grade: ")

        with open('grades.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([student_name, assignment, grade])
        print("Grade added successfully.")
    elif choice == '2':
        student_name = input("Enter student name: ")
        with open('grades.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == student_name:
                    print(f"{row[1]}: {row[2]}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    gradebook_manager()
