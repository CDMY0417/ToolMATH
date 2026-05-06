def sum_constants_times_identity(constants: list[float], size: int) -> list[list[float]]:
    return [[sum(constants) if i == j else 0 for j in range(size)] for i in range(size)]
