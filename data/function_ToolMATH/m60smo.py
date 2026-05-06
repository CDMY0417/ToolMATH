def solve_congruence(a: int, b: int, n: int) -> int:
    from sympy import mod_inverse
    a_inv = mod_inverse(a, n)
    return (b * a_inv) % n
