def find_divisors_c(number: int):
    divisors = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    return divisors
