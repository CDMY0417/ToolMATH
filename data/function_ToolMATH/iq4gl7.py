def simplify_square_root_b(n: int) -> tuple:
    factor = 1
    m = n
    for i in range(2, int(n**0.5) + 1):
        while m % (i*i) == 0:
            factor *= i
            m //= (i*i)
    return factor, m
