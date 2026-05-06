def can_form_triangle(a: int, b: int, c: int) -> bool:
    sides = sorted([a, b, c])
    return sides[0] + sides[1] > sides[2]
