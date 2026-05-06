def combinations_ba(n: int, r: int) -> int:
    if r > n:
        return 0
    r = min(r, n - r)
    num = 1
    denom = 1
    for i in range(r):
        num *= n - i
        denom *= i + 1
    return num // denom
