def last_integer_in_halving_sequence(number: int):
    while number % 2 == 0:
        number //= 2
    return number
