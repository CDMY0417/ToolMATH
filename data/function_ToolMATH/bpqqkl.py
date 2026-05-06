def am_gm_inequality_three(a: float, b: float, c: float) -> bool:
    return (a + b + c) / 3 >= (a * b * c) ** (1/3)
