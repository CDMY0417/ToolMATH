def solve_quadratic_roots(b: int, c: int) -> tuple:
    discriminant = b ** 2 - 4 * c
    if discriminant < 0:
        return ()
    sqrt_val = int(discriminant**0.5)
    return ((-b + sqrt_val) // 2, (-b - sqrt_val) // 2) if sqrt_val ** 2 == discriminant else ()
