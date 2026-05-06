def find_smallest_even_digit(digits: list[int]) -> int:
    even_digits = [d for d in digits if d % 2 == 0]
    return min(even_digits) if even_digits else None
