def generate_three_digit_palindromes() -> list:
    palindromes = []
    for a in range(1, 10):
        for b in range(10):
            palindromes.append(int(f'{a}{b}{a}'))
    return palindromes
