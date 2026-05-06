def mod_sum_of_digits_sequence(n: int, k: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += sum(int(digit) for digit in str(i))
    return total % k
