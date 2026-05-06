from collections import Counter
import math

def count_arrangements_a(solution_list: list) -> int:
    counts = Counter(solution_list)
    return math.factorial(len(solution_list)) // math.prod(math.factorial(v) for v in counts.values())
