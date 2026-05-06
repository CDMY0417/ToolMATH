def least_integer_congruence(m: int, a: int, n: int, b: int) -> int:
    i, j = 1, 1
    while True:
        n1 = m * i + a
        n2 = n * j + b
        if n1 == n2:
            return n1
        elif n1 < n2:
            i += 1
        else:
            j += 1
