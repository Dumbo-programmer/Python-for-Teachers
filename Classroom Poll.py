import matplotlib.pyplot as plt
import csv

def save_poll_results(question, votes):
    filename = "poll_results.csv"
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([question])
        for option, count in votes.items():
            writer.writerow([option, count])
        writer.writerow([])  # Blank line for separation
    print(f"Poll results saved to {filename}")

def classroom_poll():
    print("Welcome to the Classroom Poll!")
    
    # Input question and options
    question = input("Enter the poll question: ")
    options_input = input("Enter the options separated by commas: ").strip()
    if not options_input:
        print("No options entered. Please provide poll options.")
        return
    
    options = [option.strip() for option in options_input.split(',')]
    if len(options) < 2:
        print("Please enter at least two options for the poll.")
        return

    votes = {option: 0 for option in options}
    print("Enter 'done' when voting is complete.")
    
    # Polling loop
    while True:
        vote = input("Enter your vote: ").strip()
        if vote.lower() == 'done':
            break
        if vote in votes:
            votes[vote] += 1
        else:
            print(f"Invalid option. Available options are: {', '.join(options)}")
        
        # Display live vote count
        print("Current vote count:")
        for option, count in votes.items():
            print(f"{option}: {count} votes")
    
    # Plotting the results
    plt.bar(votes.keys(), votes.values(), color='skyblue')
    plt.xlabel('Options')
    plt.ylabel('Votes')
    plt.title(question)
    plt.show()
    
    # Save results to a file
    save_poll_results(question, votes)

if __name__ == "__main__":
    classroom_poll()
