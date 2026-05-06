def count_digit_palindrome(n: int) -> int:
    if n < 1:
        return 0
    half_len = (n + 1) // 2
    return (9 if n > 1 else 1) * (10 ** (half_len - 1))
