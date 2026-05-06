def smallest_integer_greater_than_cube_root(number: int) -> int:
    i = 1
    while i ** 3 <= number:
        i += 1
    return i
