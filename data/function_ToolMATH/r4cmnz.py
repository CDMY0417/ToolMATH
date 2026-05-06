def extract_last_nonzero_digit(number: int) -> int:
    while number % 10 == 0:
        number //= 10
    return number % 10
