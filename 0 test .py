import random

def generate_number():
    return random.randint(1, 10)

def get_player_input():
    while True:
        try:
            guess = int(input("Enter your guess (1-10):"))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number within the range 1 to 10.") 
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def play_round():
    target = generate_number()
    attempts = 0
    while True:
        guess = get_player_input()
        attempts = attempts + 1
        if guess < target:
            print("Too low.Give another guess.")
        elif guess > target:
            print("Too high.Give another guess.")
        else:
            print(f"Exelent! You reached the target in {attempts} attempts")
            return attempts
        


def ask_replay():
    return input("\nWould you like to play another round  (y/n ):").lower() == 'y'
def guess_the_number():
    print("\nWelcome to the guess the number experience!")
    print("The number is between 1 and 10.\n")

    total_attempts = 0
    rounds_played = 0

    while True:
        print("\n---New round (Range 1-10)---")
        attempts = play_round()
        total_attempts += attempts 
        rounds_played += 1

        if not ask_replay():
            break

    print("\n---Session Summary---")
    print(f"Total round played: {rounds_played}")
    print(f"Total attempts: {total_attempts}")
    print("Thank you for playing.Session terminated.\n")
guess_the_number()