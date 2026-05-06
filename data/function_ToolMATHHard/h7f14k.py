def sum_exponents_balanced_ternary(n: int):
    """Return sum of exponents with nonzero digits in balanced ternary."""
    if n == 0:
        return 0
    exp = 0
    total = 0
    while n != 0:
        r = n % 3
        if r == 2:
            r = -1
            n = (n + 1) // 3
        else:
            n //= 3
        if r != 0:
            total += exp
        exp += 1
    return total
