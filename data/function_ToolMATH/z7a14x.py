def is_palindrome_g(number: int) -> bool:
    s = str(number)
    return s == s[::-1]
