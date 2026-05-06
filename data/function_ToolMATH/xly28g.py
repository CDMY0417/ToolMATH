def partial_sum_of_oblong_reciprocals(n: int) -> float:
    return sum(1/(k*(k+1)) for k in range(1, n+1))
