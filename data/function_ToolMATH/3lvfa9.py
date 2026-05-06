def count_powers_of_k_less_than_n(k: int, n: int) -> int:
    count = 0
    power = 1
    while power < n:
        count += 1
        power *= k
    return count
