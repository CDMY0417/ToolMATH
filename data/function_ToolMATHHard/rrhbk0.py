def smallest_with_odd_even_divisor_counts(odd_count: int, even_count: int):
    """Return smallest n with specified odd/even divisor counts (brute force)."""
    import math
    for n in range(1, 200000):
        divs=[]
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0:
                divs.append(i)
                if i*i != n:
                    divs.append(n//i)
        odd = sum(1 for d in divs if d%2==1)
        even = len(divs) - odd
        if odd == odd_count and even == even_count:
            return n
    return None
