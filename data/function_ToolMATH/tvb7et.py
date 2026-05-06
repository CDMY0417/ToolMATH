def quadratic_mean_am_gm_inequality(values: list[float]) -> bool:
    n = len(values)
    qm = sum(x**2 for x in values) / n
    am = sum(values) / n
    if qm ** 0.5 == am:
        return True
    return False
