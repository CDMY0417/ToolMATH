def sum_of_powers_of_ten(n: int) -> int:
    return sum(10**i for i in range(n+1))
