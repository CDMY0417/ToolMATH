def first_n_composite_numbers(n: int):
    composites = []
    num = 4
    while len(composites) < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                composites.append(num)
                break
        num += 1
    return composites
