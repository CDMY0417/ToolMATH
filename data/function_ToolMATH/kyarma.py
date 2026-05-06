def find_multiples_in_range(n: int, lower: int, upper: int):
    return [x for x in range(lower, upper + 1) if x % n == 0]
