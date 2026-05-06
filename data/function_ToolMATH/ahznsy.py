def distribute_and_combine(coeffs1: list[float], terms1: list[str], coeffs2: list[float], terms2: list[str]) -> dict:
    combined = {}
    for c, t in zip(coeffs1, terms1):
        if t in combined:
            combined[t] += c
        else:
            combined[t] = c
    for c, t in zip(coeffs2, terms2):
        if t in combined:
            combined[t] += c
        else:
            combined[t] = c
    return combined
