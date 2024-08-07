#Homework Checker
import os

def homework_checker():
    print("Welcome to the Homework Checker!")
    homework_dir = input("Enter the path to the homework directory: ")

    if not os.path.isdir(homework_dir):
        print("Invalid directory.")
        return

    files = os.listdir(homework_dir)
    print("Homework files found:")
    for file in files:
        print(file)

if __name__ == "__main__":
    homework_checker()
