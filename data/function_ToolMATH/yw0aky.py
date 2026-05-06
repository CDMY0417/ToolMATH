def integer_divisors_h(n: int):
    divisors = set()
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(-i)
    return sorted(divisors)
