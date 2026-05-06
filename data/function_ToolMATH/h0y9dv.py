def distribute_terms(exp1: tuple[tuple[int, int]], exp2: tuple[tuple[int, int]]) -> list[tuple[int, int]]:
    results = []
    for term1 in exp1:
        for term2 in exp2:
            results.append((term1[0] * term2[0], term1[1] + term2[1]))
    return results
