def factors_h(n: int):
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.extend([i, n//i] if i != n//i else [i])
    return result
