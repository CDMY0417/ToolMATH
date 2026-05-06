def last_two_digit_remainder(last_digits: list[int]) -> list[int]:
    return [num % 4 for num in last_digits]
