def count_negative_x_with_integer_sqrt(N: int):
    """Return count of negative x with sqrt(x+N) positive integer."""
    count = 0
    k = 1
    while k*k < N:
        x = k*k - N
        if x < 0:
            count += 1
        k += 1
    return count
