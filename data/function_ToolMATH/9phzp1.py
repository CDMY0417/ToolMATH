def is_palindrome_f(n: int) -> bool:
    s = str(n)
    return s == s[::-1]
