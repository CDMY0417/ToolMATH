def multiples_of_n_in_range(n: int, start: int, end: int) -> list:
    return [i for i in range(start, end + 1) if i % n == 0]
