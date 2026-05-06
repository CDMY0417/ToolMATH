def divisors_of_number_a(n: int):
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(-i)
    return divisors
