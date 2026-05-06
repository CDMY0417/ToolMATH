from itertools import combinations_with_replacement, permutations

def digit_sum_n_digit_numbers(n: int, target_sum: int):
    digits = range(10)
    valid_numbers = set()
    # Generate combinations of n digits with replacement
    for combo in combinations_with_replacement(digits, n):
        if sum(combo) == target_sum:
            # Generate all distinct permutations of each valid combination
            for perm in set(permutations(combo)):
                # Convert tuple to integer, skip leading zero if any and check if valid size
                if perm[0] != 0:
                    number = int(''.join(map(str, perm)))
                    if 10**(n-1) <= number < 10**n:
                        valid_numbers.add(number)
    return list(valid_numbers)
