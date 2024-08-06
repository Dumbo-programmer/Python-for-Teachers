#Classroom Poll
import matplotlib.pyplot as plt

def classroom_poll():
    print("Welcome to the Classroom Poll!")
    question = input("Enter the poll question: ")
    options = input("Enter the options separated by commas: ").split(',')

    votes = {option.strip(): 0 for option in options}
    print("Enter 'done' when voting is complete.")

    while True:
        vote = input("Enter your vote: ")
        if vote.lower() == 'done':
            break
        if vote in votes:
            votes[vote] += 1
        else:
            print("Invalid option. Please enter a valid option.")

    plt.bar(votes.keys(), votes.values())
    plt.xlabel('Options')
    plt.ylabel('Votes')
    plt.title(question)
    plt.show()

if __name__ == "__main__":
    classroom_poll()
