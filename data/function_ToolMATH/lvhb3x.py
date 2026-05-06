def get_repeated_decimal_digit(n: int, repeating_digits: list[int]):
    if not repeating_digits:
        return None
    repeat_length = len(repeating_digits)
    return repeating_digits[(n - 1) % repeat_length]
