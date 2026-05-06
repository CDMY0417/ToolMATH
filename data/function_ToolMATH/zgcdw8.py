def count_nonnegative_balanced_ternary_integers(n: int) -> int:
    max_bound = 3 ** n / 2
    num_positive = int(max_bound)
    return num_positive + 1
