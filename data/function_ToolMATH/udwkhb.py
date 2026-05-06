def is_abundant_number(n: int) -> bool:
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum > n
