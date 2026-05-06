def qm_am_inequality_d(numbers: list[float]) -> tuple:
    n = len(numbers)
    am = sum(numbers) / n
    qm = (sum(x**2 for x in numbers) / n)**0.5
    return am, qm
