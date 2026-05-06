def find_extreme_values_satisfying_cube_condition(lo: int, hi: int) -> tuple:
    n = 0
    while n**3 <= lo:
        n += 1
    smallest = n - 1
    while n**3 < hi:
        n += 1
    largest = n - 1
    return smallest, largest
