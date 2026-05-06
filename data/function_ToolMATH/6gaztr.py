def two_digit_palindrome(n: int) -> int:
    s = str(n)
    return int(s + s[::-1])
