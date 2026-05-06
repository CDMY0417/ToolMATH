def is_palindrome_d(number: int) -> bool:
    s = str(number)
    return s == s[::-1]
