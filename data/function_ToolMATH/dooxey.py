def number_of_integers_with_restricted_digits(base: int, power: int, forbidden_digits: list[int]) -> int:
    allowed_digits = [d for d in range(base) if d not in forbidden_digits]
    return len(allowed_digits) ** power
