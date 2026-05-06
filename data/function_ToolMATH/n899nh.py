
def largest_factor_below_limit(number: int, limit: int) -> int:
    for i in range(limit-1, 0, -1):
        if number % i == 0:
            return i
    return 1
