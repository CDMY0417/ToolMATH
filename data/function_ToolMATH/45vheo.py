def simplify_radical(n: int) -> (int, int):
    factor, simplified_n = 1, n
    for i in range(2, int(n ** 0.5) + 1):
        count = 0
        while simplified_n % i == 0:
            simplified_n //= i
            count += 1
        factor *= i ** (count // 2)
        simplified_n *= i ** (count % 2)
    return factor, simplified_n
