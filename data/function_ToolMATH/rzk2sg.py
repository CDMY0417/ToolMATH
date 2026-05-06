def sum_of_powers_of_three(n: int) -> int:
    return sum(3**i for i in range(n + 1))
