def years_with_remainder(start: int, end: int, remainder: int, divisor: int):
    results = []
    year = start - (start % divisor) + remainder
    if year < start:
        year += divisor
    while year <= end:
        results.append(year)
        year += divisor
    return results
