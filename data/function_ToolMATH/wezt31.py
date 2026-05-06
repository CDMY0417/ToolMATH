def integer_divisors_g(n: int):
    divisors = set()
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(-i)
    return divisors
