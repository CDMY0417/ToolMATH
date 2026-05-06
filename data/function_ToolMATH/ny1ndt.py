def divisors_e(n: int) -> set:
    divs = set()
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(-i)
    return divs
