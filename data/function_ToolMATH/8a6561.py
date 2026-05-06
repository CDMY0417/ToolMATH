def carmichael_function(n: int) -> int:
    from math import gcd
    if n == 1:
        return 1
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            loop_length = 1
            while pow(i, loop_length, n) != 1:
                loop_length += 1
            result = max(result, loop_length)
    return result
