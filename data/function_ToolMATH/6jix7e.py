def is_palindrome_i(num: int) -> bool:
    s = str(num)
    return s == s[::-1]
