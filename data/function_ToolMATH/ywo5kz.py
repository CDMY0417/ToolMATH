def factors_i(n: int) -> list:
    fact_set = set()
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            fact_set.add(i)
            fact_set.add(-i)
    return sorted(fact_set)
