def alternating_digit_sum(digits: list[int]) -> int:
    return sum(d if i % 2 == 0 else -d for i, d in enumerate(digits))
