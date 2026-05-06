def max_of_x_times_one_minus_x_power(n: int):
    # Max of x(1-x)^n on [0,1] is (1/(n+1))*(n/(n+1))^n
    if n < 1:
        return 0.0
    return (1/(n+1)) * ((n/(n+1))**n)
