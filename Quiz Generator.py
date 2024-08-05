#Quiz Generator
import random

def quiz_generator():
    print("Welcome to the Quiz Generator!")
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "What year did the Titanic sink?", "answer": "1912"}
    ]

    num_questions = int(input("Enter the number of questions for the quiz: "))
    selected_questions = random.sample(questions, num_questions)

    for i, q in enumerate(selected_questions, start=1):
        print(f"Q{i}: {q['question']}")
        input("Your answer: ")
        print(f"Correct answer: {q['answer']}")
    print("Quiz completed.")

if __name__ == "__main__":
    quiz_generator()
