def divisors_c(n: int) -> set[int]:
    result = set()
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.update({i, -i})
    return result
