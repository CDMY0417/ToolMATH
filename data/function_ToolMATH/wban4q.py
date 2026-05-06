def candidate_values_with_units_digit(units_digit: int, divisor: int, limit: int) -> list:
    candidates = []
    n = units_digit
    while n <= limit:
        if n % divisor == 0:
            candidates.append(n)
        n += 10
    return candidates
