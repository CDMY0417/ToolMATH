def generate_2_5_factor_numbers(limit: int) -> list:
    numbers = set()
    m, n = 0, 0
    value = 2**m * 5**n
    while value <= limit:
        n = 0
        while 2**m * 5**n <= limit:
            numbers.add(2**m * 5**n)
            n += 1
        m += 1
        value = 2**m
    return sorted(numbers)
