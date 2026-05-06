def is_palindrome_a(n: int) -> bool:
    s = str(n)
    return s == s[::-1]
