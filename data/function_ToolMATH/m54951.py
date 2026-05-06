def simplest_radical_form(number: int) -> str:
    from math import isqrt
    factor = 1
    for i in range(2, isqrt(number) + 1):
        while number % (i * i) == 0:
            number //= i * i
            factor *= i
    return f'{factor}\sqrt{{{number}}}' if number != 1 else str(factor)
