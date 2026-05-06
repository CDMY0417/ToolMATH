def sum_fibonacci_power_series(r: float):
    """Return sum of Fibonacci series for r>phi."""
    # Sum_{n>=0} F_n x^n = x/(1-x-x^2). Here x=1/r
    x = 1.0 / r
    return x / (1 - x - x*x)
