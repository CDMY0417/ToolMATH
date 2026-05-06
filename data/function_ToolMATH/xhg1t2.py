def solve_linear_congruence_b(a: int, b: int, n: int):
    def extended_gcd(aa, bb):
        if bb == 0:
            return aa, 1, 0
        g, x1, y1 = extended_gcd(bb, aa % bb)
        x = y1
        y = x1 - (aa // bb) * y1
        return g, x, y

    g, x0, _ = extended_gcd(a, n)
    if b % g != 0:
        return None  # No solution
    return (x0 * (b // g)) % n
