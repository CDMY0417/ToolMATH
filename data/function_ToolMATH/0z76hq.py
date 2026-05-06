def piecewise_tax(income: float) -> float:
    if 0 <= income <= 20000:
        return 0
    elif 20000 < income <= 45000:
        return 0.05 * (income - 20000)
    elif 45000 < income <= 80000:
        return 1250 + 0.1 * (income - 45000)
    elif 80000 < income <= 130000:
        return 4750 + 0.15 * (income - 80000)
    else:
        return 12250 + 0.2 * (income - 130000)
