import random

def display_rules():
    print("\n---Game rules---")
    print("Rock beats Scissors")
    print("Scissors beats Papper")
    print("Papper beats Rock\n")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "sissors" and computer == "papper") or \
         (user == "papper" and computer == "rock"):
        return "user"
    else:
        return "computer"
    
def rock_paper_scissors():
    total_choices = ["rock", "paper", "scissors"]

    while True:
        user_score = 0
        computer_score = 0
        round_number = 1
         
        print("\n Welcome to Rock-Papper-Scissors Game!")
        print("Type 'rules' to see how to play, or 'quit' to exit the game")

        while True:
            print(f"\n--- Round {round_number} ---")
            print("Available choices: rock, papper, scissors.")
            user_choice = input("Enter your choice: ").lower()

            if user_choice == "quit":
                print("\nThanks for playing")
                print(f"Final score => You: {user_score} | Computer: {computer_score}\n")
                break
            elif user_choice == "rules":
                display_rules()
                continue
            elif user_choice not in total_choices:
                print("Invalid input. Please enter rock, papper, scissors.")
                continue

            computer_choice = random.choice(total_choices)
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)

            if result == "tie":
                print("It's a tie!")
            elif result == "user":
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

            print(f"Current Scores => You: {user_score}  | Computer: {computer_score}")
            round_number += 1

        play_again = input("Would you like to play again? (yes/no):").lower()
        if play_again != "yes":
            print("Goodbye!")
            break




