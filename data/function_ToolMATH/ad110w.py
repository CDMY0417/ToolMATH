def consecutive_primes_differences(integers: list[int]) -> list[int]:
    return [integers[i+1] - integers[i] for i in range(len(integers) - 1)]
