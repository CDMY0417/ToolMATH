def cube_number_n_times(base: int, n: int):
    result = base
    for _ in range(n):
        result = result ** 3
    return result
