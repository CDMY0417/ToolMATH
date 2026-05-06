def is_palindrome_e(n: int) -> bool:
    s = str(n)
    return s == s[::-1]
