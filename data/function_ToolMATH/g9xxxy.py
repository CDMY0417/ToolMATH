def count_perfect_square_offsets(start: int, end: int) -> int:
    count = 0
    for n in range(start, end + 1):
        if int((n + 1) ** 0.5) ** 2 == n + 1:
            count += 1
    return count
