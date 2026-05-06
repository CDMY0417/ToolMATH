def linear_recurrence_with_linear_term(n: int, f1: float, f2: float):
    """Return f(n) for recurrence f(n)=f(n-1)-f(n-2)+n."""
    if n == 1:
        return f1
    if n == 2:
        return f2
    a = f1
    b = f2
    for k in range(3, n+1):
        a, b = b, b - a + k
    return b
