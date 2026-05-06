def factors(n: int):
    n = abs(n)
    result = set()
    for i in range(1, n + 1):
        if n % i == 0:
            result.add(i)
            result.add(-i)
    return sorted(result)
