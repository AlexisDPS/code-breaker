




import random
import check_input


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
    print(f"Exact matches: {results[0]}")
    print(f"Misplaced matches: {results[1]}")



def main():
    computers_code = generate_code()
    print(f"the code is: {computers_code}")
    in_game = True
    attempt_number = 0
    print("--Code Breaker!--")
    print("Crack the 4-digit code within 8")
    print("attempts to open the safe.")
    print("Each digit is between 1-6.")
    print()
    while in_game:
        won = False
        for i in range(8):
            attempt_number += 1
            print(f"Attempt #{attempt_number}")
            guess = get_guess()
            results = check_guess(computers_code, guess)
            display_results(results)
            if results[0] == 4:
                won = True
                print("You cracked the code!")
                in_game = False
        if not won:
            print(f"The correct code was: {computers_code}")
            print("You lost.")
            in_game = False



main()