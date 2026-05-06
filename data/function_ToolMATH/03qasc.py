def generate_cubes(max_value: int):
    cubes = []
    n = 1
    while n ** 3 <= max_value:
        cubes.append(n ** 3)
        n += 1
    return cubes
