def vieta_roots(sum_of_roots: float, product_of_roots: float) -> tuple:
    
    a = 1
    b = -sum_of_roots
    c = product_of_roots
    discriminant = b**2 - 4*a*c
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return (root1, root2)
