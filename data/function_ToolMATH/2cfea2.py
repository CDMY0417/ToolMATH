def find_k_pi_solutions(k_values: list[int], range_min: float, range_max: float) -> list[float]:
    from math import pi
    solutions = []
    for k in k_values:
        x = k * pi / 4
        if range_min <= x <= range_max:
            solutions.append(x)
    return solutions
