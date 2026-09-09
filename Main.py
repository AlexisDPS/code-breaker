# Group 10
# Broden Black
# Alexis De Paz Salazar
# This lab is a code breaking game where the user gets 8 chances to guess a 4-digit code. There are no duplicate numbers in the code and each number is between 1 and 6. Each attempt gives the user feedback and if the code is guessed in the 8 attempts, the user wins.

import random
import check_input

# TODO: Add docstrings to all functions. Document all parameters and return values.
# TODO: Add brief comments (# style) within your functions to describe sections of code.

def generate_code():
    code = []
    for i in range(4):
        new_digit = random.randint(1, 6)
        while new_digit in code:
            new_digit = random.randint(1, 6)
        code.append(new_digit)
    return code


def get_guess():
    guess = []
    for i in range(4):
        new_digit = check_input.get_int_range(f"- Enter digit {i + 1}: ", 1, 6)
        while new_digit in guess:
            print("Invalid input - cannot enter a duplicate value.")
            new_digit = check_input.get_int_range(f"- Enter digit {i + 1}: ", 1, 6)
        guess.append(new_digit)
    return guess



def check_guess(code, guess):
    exact_matches = 0
    misplaced_matches = 0
    for i in range(4):
        if code[i] == guess[i]:
            exact_matches += 1
        else:
            if guess[i] in code:
                misplaced_matches += 1
    return [exact_matches, misplaced_matches]
        


def display_results(results):
    print("Results:")
    print(f"- Exact matches: {results[0]}")
    print(f"- Misplaced matches: {results[1]}")



def main():
    computers_code = generate_code()
    in_game = True
    attempt_number = 0
    print("--Code Breaker!--")
    print("Crack the 4-digit code within 8 attempts to open the safe.")
    print("Each digit is between 1-6.")
    print()
    while in_game:
        won = False
        while attempt_number < 8 and not won:  # TODO: doesn't quit after winning
            attempt_number += 1
            print(f"Attempt #{attempt_number}")
            guess = get_guess()
            results = check_guess(computers_code, guess)
            print(f"Your guess: {guess}")
            display_results(results)
            if results[0] == 4:
                won = True
                print()
                print("You have cracked the code!")
            print()
        if not won:
            print(f"The correct code was: {computers_code}")
            print("You lost.")
            in_game = False



main()