#Class Average Calculator
import csv

def class_average_calculator():
    print("Welcome to the Class Average Calculator!")
    assignment = input("Enter the assignment name: ")

    total_grade = 0
    count = 0

    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] == assignment:
                total_grade += float(row[2])
                count += 1

    if count == 0:
        print("No grades found for the assignment.")
        return

    average_grade = total_grade / count
    print(f"Average Grade for {assignment}: {average_grade:.2f}")

if __name__ == "__main__":
    class_average_calculator()
