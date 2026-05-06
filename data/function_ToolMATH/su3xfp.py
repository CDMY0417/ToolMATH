def count_perfect_squares_in_range_b(lo: int, hi: int) -> int:
    count = 0
    start = int(lo ** 0.5)
    end = int(hi ** 0.5)
    for i in range(start, end + 1):
        square = i * i
        if square >= lo and square <= hi:
            count += 1
    return count
