def count_multiples_f(lo: int, hi: int, divisor: int):
    return sum(1 for i in range(lo+1, hi) if i % divisor == 0)
