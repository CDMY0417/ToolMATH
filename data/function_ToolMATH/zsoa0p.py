def sin_zero_points(n_values: list[int]) -> list[float]:
    zero_points = set()
    for n in n_values:
        for k in range(0, n + 1):
            zero_points.add(k / n)
    return sorted(zero_points)
