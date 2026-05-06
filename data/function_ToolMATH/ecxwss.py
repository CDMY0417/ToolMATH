def factor_sum_of_product(target: int, sum_value: int) -> tuple:
    for i in range(1, int(target**0.5) + 1):
        if target % i == 0:
            j = target // i
            if i + j == sum_value:
                return (i, j)
    return None
