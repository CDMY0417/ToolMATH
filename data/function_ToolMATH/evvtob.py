def count_perfect_squares(limit: int) -> int:
    count = 0
    for i in range(1, int(limit**0.5) + 1):
        if i * i < limit:
            count += 1
    return count
