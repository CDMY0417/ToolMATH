def find_integer_with_remainders(remainders: list[int], divisors: list[int]) -> int:
    x = remainders[0]
    step = divisors[0]
    while True:
        if all(x % divisors[i] == remainders[i] for i in range(len(divisors))):
            return x
        x += step
