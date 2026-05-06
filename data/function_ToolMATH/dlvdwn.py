def count_factors_less_than(n: int, threshold: int) -> int:
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i < threshold:
                count += 1
            if n // i < threshold and n // i != i:
                count += 1
    return count
