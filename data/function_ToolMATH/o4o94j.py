def sum_of_divisors_b(n: int) -> int:
    sum_div = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            temp_sum = 1
            power = 1
            while n % factor == 0:
                power *= factor
                temp_sum += power
                n //= factor
            sum_div *= temp_sum
        factor += 1
    if n > 1:
        sum_div *= (1 + n)
    return sum_div
