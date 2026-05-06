def compound_interest_greater_than(rate: float, multiple: float) -> int:
    t = 0
    while (1 + rate) ** t <= multiple:
        t += 1
    return t
