def count_multiples_of_n(n: int, start: int, end: int) -> int:
    return len([x for x in range(start, end + 1) if x % n == 0])
