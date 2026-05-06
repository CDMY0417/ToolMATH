def largest_divisor_less_than(number: int, max_limit: int):
    for i in range(max_limit - 1, 0, -1):
        if number % i == 0:
            return i
    return None
