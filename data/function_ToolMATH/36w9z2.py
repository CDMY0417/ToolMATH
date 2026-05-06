def quadratic_factors_from_inequality(a: float, b: float, c: float):
    import math
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return []
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b - sqrt_discriminant) / (2 * a)
    root2 = (-b + sqrt_discriminant) / (2 * a)
    if a > 0:
        return sorted((root1, root2))  # a (convex) parabola opens up, correct interval is between roots
    else:
        return [(-math.inf, root1), (root2, math.inf)]  # a (concave) parabola opens down, intervals are outside the roots
