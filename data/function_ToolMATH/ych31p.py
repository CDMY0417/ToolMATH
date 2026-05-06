def check_divisibility(factorial_factors: dict, divisor_factors: dict) -> bool:
    for prime, exp in divisor_factors.items():
        if prime not in factorial_factors or factorial_factors[prime] < exp:
            return False
    return True
