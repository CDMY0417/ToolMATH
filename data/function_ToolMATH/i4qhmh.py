def largest_even_less_than(n: int) -> int:
    return n - 1 if n % 2 != 0 else n - 2
