def is_sixth_power(n: int) -> bool:
    root = round(n**(1/6))
    return root**6 == n
