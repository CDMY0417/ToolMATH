def generate_palindromes(start: int, end: int, n: int):
    palindromes = []
    for i in range(start, end + 1):
        if len(str(i)) == n and str(i) == str(i)[::-1]:
            palindromes.append(i)
    return palindromes
