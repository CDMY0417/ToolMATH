def extract_and_simplify_root(n: int) -> tuple[int, int]:
    import math
    k = int(math.sqrt(n))
    while k > 1:
        if n % (k * k) == 0:
            return k, n // (k * k)
        k -= 1
    return 1, n
