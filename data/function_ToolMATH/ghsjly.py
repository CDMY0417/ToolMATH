def count_odd_choices(digits: list[int]) -> int:
    odd_digits = [d for d in digits if d % 2 != 0]
    return len(odd_digits)
