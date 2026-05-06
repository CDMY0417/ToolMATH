def count_palindromes_containing_digit(palindromes: list[int], digit: int) -> int:
    count = 0
    for palindrome in palindromes:
        if str(digit) in str(palindrome):
            count += 1
    return count
