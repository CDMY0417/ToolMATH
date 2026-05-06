def divisors_of_number_c(number: int) -> list:
    divisors = []
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            divisors.extend([i, -i])
    return divisors
