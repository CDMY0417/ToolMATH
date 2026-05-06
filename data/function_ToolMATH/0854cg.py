def is_palindrome_h(num: int) -> bool:
    s = str(num)
    return s == s[::-1]
