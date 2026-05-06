def cube_sum_identity(a: float, b: float, c: float):
    part1 = a**3 + b**3 + c**3
    part2 = 3 * (a**2*b + a*b**2 + b**2*c + b*c**2 + c**2*a + c*a**2)
    part3 = 6 * a * b * c
    return part1 + part2 + part3
