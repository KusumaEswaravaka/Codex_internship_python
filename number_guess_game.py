import random

def guess_num(lower_bound, upper_bound):
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct Guess!"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"

def play_game():
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    max_attempts = 10
    secret_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = guess_num(lower_bound, upper_bound)
        result = check_guess(guess, secret_number)

        if result == "Correct Guess!":
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number was {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()
