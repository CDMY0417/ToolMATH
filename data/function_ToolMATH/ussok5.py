def is_palindrome_j(num: int) -> bool:
    s = str(num)
    return s == s[::-1]
