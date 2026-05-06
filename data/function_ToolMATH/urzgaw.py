def is_palindrome_c(n: int) -> bool:
    s = str(n)
    return s == s[::-1]
