def qm_am_inequality_a(values: list[float]) -> bool:
    qm = (sum(value**2 for value in values) / 4) ** 0.5
    am = sum(values) / 4
    return qm >= am
