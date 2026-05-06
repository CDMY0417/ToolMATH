def is_palindrome_l(n: int) -> bool:
    s = str(n)
    return s == s[::-1]
