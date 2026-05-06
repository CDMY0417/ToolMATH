def count_perfect_sixth_powers(limit: int) -> int:
    count = 0
    i = 1
    while i ** 6 < limit:
        count += 1
        i += 1
    return count
