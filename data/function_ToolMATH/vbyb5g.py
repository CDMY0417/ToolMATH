def is_divisible_by_11_b(digits: list[int]) -> bool:
    return abs(sum(digits[::2]) - sum(digits[1::2])) % 11 == 0
