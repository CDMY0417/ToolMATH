def is_palindrome_b(num: int) -> bool:
    s = str(num)
    return s == s[::-1]
