def power_in_range(a: int, low: int, high: int) -> list:
    n = 0
    result = []
    while True:
        power = a ** n
        if power > high:
            break
        if power >= low:
            result.append(n)
        n += 1
    return result
