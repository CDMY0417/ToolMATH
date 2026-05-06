def product_of_odds_less_than(limit: int):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    product = 1
    for number in range(3, limit, 2):
        if is_prime(number):
            product *= number
    return product
