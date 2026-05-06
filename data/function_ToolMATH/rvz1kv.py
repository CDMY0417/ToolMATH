def square_of_difference_d(n: int, k: int) -> int:
    term1 = 10**(2*n)
    term2 = -2 * k * 10**n
    term3 = k**2
    return term1 + term2 + term3
