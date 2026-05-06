def count_integers_ending_with(start: int, end: int, base: int) -> int:
    count = 0
    for i in range(start, end + 1):
        if (i + 1) % base == 0:
            count += 1
    return count
