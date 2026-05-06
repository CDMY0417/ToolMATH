def possible_last_two_digits(target_units: int, divisor: int):
    candidates = []
    for tens in range(10):
        if (tens * 10 + target_units) % divisor == 0:
            candidates.append(tens)
    return candidates
