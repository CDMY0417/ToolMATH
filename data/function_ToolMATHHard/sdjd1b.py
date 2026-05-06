def mod_exp_difference(a: int, b: int, n: int, m: int):
    return (pow(a, n, m) - pow(b, n, m)) % m
