import os
from datetime import datetime

def list_files(directory, extension=None):
    """Lists files in the directory with a specific extension."""
    if extension:
        return [file for file in os.listdir(directory) if file.endswith(extension)]
    return os.listdir(directory)

def check_submissions(directory, students):
    """Checks which students have submitted their homework."""
    submitted_files = list_files(directory)
    submitted_students = [file.split('.')[0] for file in submitted_files]

    missing_students = [student for student in students if student not in submitted_students]
    return submitted_files, missing_students

def homework_checker():
    print("Welcome to the Homework Checker!")
    homework_dir = input("Enter the path to the homework directory: ")
    
    if not os.path.isdir(homework_dir):
        print("Invalid directory.")
        return
    
    extension = input("Enter the file extension to filter (e.g., .pdf, .docx) or press Enter to show all: ").strip()
    students = input("Enter student names separated by commas (leave blank if not checking): ").split(',')

    # List files with optional filtering
    files = list_files(homework_dir, extension if extension else None)
    
    if files:
        print("\nHomework files found:")
        for file in files:
            file_path = os.path.join(homework_dir, file)
            last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{file} (Last modified: {last_modified})")
    else:
        print("\nNo files found.")

    # Check submissions
    if students:
        students = [student.strip() for student in students if student.strip()]
        _, missing_students = check_submissions(homework_dir, students)
        if missing_students:
            print("\nMissing submissions:")
            for student in missing_students:
                print(student)
        else:
            print("\nAll students have submitted their homework.")

if __name__ == "__main__":
    homework_checker()
