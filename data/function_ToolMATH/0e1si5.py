def roots_ending_in_digits(limit: int, digits: list[int]) -> list[int]:
    roots = []
    i = 1
    while i < limit:
        if i % 10 in digits:
            roots.append(i)
        i += 1
    return roots
