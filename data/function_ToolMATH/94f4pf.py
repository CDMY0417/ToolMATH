def compute_f(n: int) -> int:
    if n % 2 == 0:
        return n**2 - 4*n - 1
    else:
        return n**2
