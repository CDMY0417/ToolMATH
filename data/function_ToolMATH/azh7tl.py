def proper_divisors(n: int) -> list:
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors
