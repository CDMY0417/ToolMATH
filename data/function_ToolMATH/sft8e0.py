def sum_of_first_n_integers_modulo(n: int, m: int):
    total_sum = (n * (n - 1)) // 2
    return total_sum % m
