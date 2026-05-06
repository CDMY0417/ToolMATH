def count_multiples_in_range_e(start: int, end: int, divisor: int) -> int:
    count = 0
    for i in range(start, end + 1):
        if i % divisor == 0:
            count += 1
    return count
