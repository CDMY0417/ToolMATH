def is_divisible_by_11(digits: list[int]) -> bool:
    return (sum(digits[::2]) - sum(digits[1::2])) % 11 == 0
