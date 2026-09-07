




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
    for i in range(4):
        if code[i] == guess[i]:
            exact_matches += 1
        if guess[i] in code and code[i] != guess[i]:
            misplaced_matches += 1
    return [exact_matches, misplaced_matches]
        


def display_results(results):
    print(f"Exact matches: {results[0]}")
    print(f"Misplaced matches: {results[1]}")



def main():
    pass

main()