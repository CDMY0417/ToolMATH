def is_right_triangle(a: int, b: int, c: int) -> bool:
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
