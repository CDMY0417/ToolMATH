def max_possible_sum(n: int, max_value: int) -> int:
    return sum(range(max_value - n + 1, max_value + 1))
