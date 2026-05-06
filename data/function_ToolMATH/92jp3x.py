def is_palindrome_k(number: int) -> bool:
    s = str(number)
    return s == s[::-1]
