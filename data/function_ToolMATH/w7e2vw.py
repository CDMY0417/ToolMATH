def integer_divisors_f(n: int):
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.extend([i, -i])
    return divisors
