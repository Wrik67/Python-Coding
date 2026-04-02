import random

def generate_number():
    return random.randint(1, 10)

def get_player_input():
    while True:
        try:
            guess = int(input("Enter a number (1 to 10):"))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number within the range of 1 to 10")

        except ValueError:
                print("Invalid input. Plese enter a valid number.")

def play_round():
     target = generate_number()
     attepts = 0
     while True:
          target = get_player_input()
          attempts = attempts + 1
          if guess < target:
               print("Too low try another attempt.")
          elif guess > target:
               print("Too high try another attempt.")
          else:
               