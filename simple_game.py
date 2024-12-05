///This code initializes a number guessing game where the player tries to guess a randomly selected number between 1 and 100. The game uses loops and functions to handle the game flow and user input.///
import random

def initialize_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    return random.randint(1, 100)

def get_user_input():
    return int(input("Enter your guess: "))

def game_logic(secret_number):
    attempts = 0
    while True:
        guess = get_user_input()
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def main():
    secret_number = initialize_game()
    game_logic(secret_number)

if __name__ == "__main__":
    main()
