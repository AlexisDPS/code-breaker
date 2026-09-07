




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
    pass


def display_results(results):
    pass



def main():
    pass

main()