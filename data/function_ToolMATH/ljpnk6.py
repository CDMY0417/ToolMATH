def cubes_less_than_or_equal_to(limit: int):
    cubes = [n**3 for n in range(1, limit + 1)]
    return [cube for cube in cubes if int(cube ** (1/3)) ** 3 == cube]
