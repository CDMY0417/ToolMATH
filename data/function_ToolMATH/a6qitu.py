def sum_of_remainders_mod_n(remainders: list[int], n: int) -> int:
    total_remainder = sum(remainders)
    return total_remainder % n
