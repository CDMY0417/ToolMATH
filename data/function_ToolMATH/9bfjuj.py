def expand_binomial_products(a1: int, b1: int, a2: int, b2: int):
    ax2 = a1 * a2
    bx = a1 * b2 + b1 * a2
    c = b1 * b2
    return ax2, bx, c
