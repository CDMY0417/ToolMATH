def quadratic_polynomial(c: float, root1: float, root2: float) -> str:
    a = c
    b = -c * (root1 + root2)
    c_const = c * root1 * root2
    return f'{a}x^2 + {b}x + {c_const}'
