def count_n_digit_numbers(n: int) -> int:
    if n <= 0:
        return 0
    return 9 * (10 ** (n - 1))
