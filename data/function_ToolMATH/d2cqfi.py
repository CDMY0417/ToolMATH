def square_root_in_simplest_radical_form(n: int):
    import math
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    inside, outside = 1, 1
    for factor in set(factors):
        count = factors.count(factor)
        outside *= factor ** (count // 2)
        inside *= factor ** (count % 2)
    return outside, inside
