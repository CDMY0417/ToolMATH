def roots_to_standard_form(root1: float, root2: float) -> tuple:
    a = 1
    b = -a * (root1 + root2)
    c = a * root1 * root2
    return (a, b, c)
