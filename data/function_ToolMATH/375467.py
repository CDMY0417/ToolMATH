def count_distinct_numbers(start: int, end: int, divisor: int) -> int:
    seen = set()
    for n in range(start, end + 1):
        seen.add((n ** 2) // divisor)
    return len(seen)
