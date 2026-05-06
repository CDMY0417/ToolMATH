def integer_divisors_k(n: int) -> set[int]:
    n = abs(n)
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors
