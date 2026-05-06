def generate_divisors(number: int):
    divisors = set()
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(-i)
    return divisors
