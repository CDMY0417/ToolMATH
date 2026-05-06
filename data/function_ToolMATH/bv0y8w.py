def cubic_polynomial_coefficients(root1: float, root2: float, root3: float):
    a = 1
    b = -(root1 + root2 + root3)
    c = root1*root2 + root2*root3 + root3*root1
    d = -root1*root2*root3
    return (a, b, c, d)
