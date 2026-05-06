def fibonacci_like_term(n: int, a1: int, a2: int) -> int:
    if n == 1:
        return a1
    elif n == 2:
        return a2
    else:
        prev2, prev1 = a1, a2
        for _ in range(3, n+1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        return current
