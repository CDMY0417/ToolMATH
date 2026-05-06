def odd_perfect_squares_in_range(start: int, end: int) -> int:
    count = 0
    for i in range(1, int(end**0.5) + 1):
        square = i * i
        if square >= start and square <= end and square % 2 == 1:
            count += 1
    return count
