def radical_simplification(number: int) -> str:
    factor = 1
    for i in range(2, int(number**0.5) + 1):
        while number % (i * i) == 0:
            factor *= i
            number //= i * i
    return f'{factor}\sqrt{{{number}}}' if number > 1 else str(factor)
