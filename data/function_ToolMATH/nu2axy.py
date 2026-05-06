def compute_f_a(n: int) -> int:
    if n % 2 == 0:
        return n**2 - 3*n + 1
    else:
        return n**2 + 1
