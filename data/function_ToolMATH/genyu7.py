def distribute(a1: int, b1: int, a2: int, b2: int):
    part1 = a1 * a2
    part2 = a1 * b2 + a2 * b1
    part3 = b1 * b2
    return part1, part2, part3
