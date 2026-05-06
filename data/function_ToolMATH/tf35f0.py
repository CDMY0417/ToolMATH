def find_roots_of_quadratic_c(lambda_val: float):
    a = lambda_val ** 2
    b = -(lambda_val ** 2 + lambda_val)
    c = lambda_val + 1
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return []
    sqrt_discriminant = discriminant ** 0.5
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return [root1, root2]
