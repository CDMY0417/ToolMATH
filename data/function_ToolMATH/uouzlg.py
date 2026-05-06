def solve_for_divisor_given_quotient_and_remainder(dividend: int, quotient: int, remainder: int) -> int:
    divisor = (dividend - remainder) // quotient
    return divisor
