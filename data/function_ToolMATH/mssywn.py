def binary_to_fraction(binary_string: str) -> float:
    fraction = 0
    for i, digit in enumerate(binary_string):
        if digit == '1':
            fraction += 1 / (2 ** (i + 1))
    return fraction
