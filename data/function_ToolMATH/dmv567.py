def binomial_coefficient_dd(n: int, k: int, known: dict):
    while (n, k) not in known:
        for i in range(1, n+1):
            for j in range(i+1):
                if j == 0 or j == i:
                    known[(i, j)] = 1
                elif (i, j) not in known:
                    known[(i, j)] = known.get((i-1, j), 0) + known.get((i-1, j-1), 0)
    return known[(n, k)]
