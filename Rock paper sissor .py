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