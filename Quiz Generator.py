import random

def quiz_generator():
    print("Welcome to the Quiz Generator!")
    
    # Define questions with multiple choice options
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["Paris", "Rome", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "choices": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "choices": ["Harper Lee", "Mark Twain", "F. Scott Fitzgerald", "J.K. Rowling"],
            "answer": "Harper Lee"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Jupiter"
        },
        {
            "question": "What year did the Titanic sink?",
            "choices": ["1905", "1912", "1918", "1923"],
            "answer": "1912"
        }
    ]

    num_questions = int(input("Enter the number of questions for the quiz: "))
    selected_questions = random.sample(questions, num_questions)
    score = 0

    for i, q in enumerate(selected_questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        random.shuffle(q['choices'])  # Shuffle answer choices
        
        for idx, choice in enumerate(q['choices'], start=1):
            print(f"{idx}. {choice}")
        
        user_answer = input("Your answer (enter the number): ")
        correct_answer = q['answer']
        correct_index = q['choices'].index(correct_answer) + 1
        
        if int(user_answer) == correct_index:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {correct_index}. {correct_answer}")
    
    print(f"\nQuiz completed. Your score: {score}/{num_questions}")

if __name__ == "__main__":
    quiz_generator()
