def compute_g_values(domain: list[float], f_values: list[float]) -> list[float]:
    return [f - x for x, f in zip(domain, f_values)]
