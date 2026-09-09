




import random
import check_input


def generate_code():
    code = []
    for i in range(4):
        code.append(random.randint(1, 6))
    return code


def get_guess():
    guess = []
    for i in range(4):
        guess.append(check_input.get_int_range(f"- Enter digit {i + 1}: ", 1, 6))
    return guess



def check_guess(code, guess):
    exact_matches = 0
    misplaced_matches = 0
    unmatched_code = []
    unmatched_guess = []
    for i in range(4):
        if code[i] == guess[i]:
            exact_matches += 1
        else:
            unmatched_code.append(code[i])
            unmatched_guess.append(guess[i])
    if len(unmatched_code) > 0:
        for num in unmatched_guess:
            if num in unmatched_code:
                unmatched_code.remove(num)
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
            print(f"Attempt number: {attempt_number}")
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