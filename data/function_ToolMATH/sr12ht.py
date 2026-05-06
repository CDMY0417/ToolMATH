def factors_e(n: int):
    result = set()
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.add(i)
            result.add(-i)
    return result
