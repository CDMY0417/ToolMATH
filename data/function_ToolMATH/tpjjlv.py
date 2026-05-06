def is_divisible_by_four_a(num: int) -> bool:
    last_two_digits = num % 100
    return last_two_digits % 4 == 0
