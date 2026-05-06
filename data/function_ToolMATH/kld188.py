def generate_cubes_less_than(limit: int) -> list:
    cubes = []
    i = 1
    while i ** 3 < limit:
        cubes.append(i ** 3)
        i += 1
    return cubes
