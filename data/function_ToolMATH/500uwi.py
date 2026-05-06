def find_factors(n: int) -> list[int]:
    return [i for i in range(1, n+1) if n % i == 0]
