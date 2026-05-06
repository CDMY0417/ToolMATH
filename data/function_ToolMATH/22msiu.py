def lucas_number(n: int) -> int:
    L0, L1 = 2, 1
    if n == 0:
        return L0
    elif n == 1:
        return L1
    for _ in range(2, n + 1):
        L0, L1 = L1, L0 + L1
    return L1
