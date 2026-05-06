def simplify_square_root_a(n: int) -> str:
    import math
    factor = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % (i * i) == 0:
            factor *= i
            n //= i * i
    return '{}√{}'.format(factor, n) if factor > 1 else '√{}'.format(n)
