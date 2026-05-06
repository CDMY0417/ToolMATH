def find_unique_n_for_cube_sum(target: int, step: int, n_min: int, n_max: int, x_min: int, x_max: int):
    """Return n if a unique n in [n_min,n_max] yields an integer x solution within bounds."""
    solutions = []
    for n in range(n_min, n_max + 1):
        for x in range(x_min, x_max + 1):
            s = 0
            for k in range(n + 1):
                s += (x + step * k) ** 3
            if s == target:
                solutions.append(n)
                break
    uniq = sorted(set(solutions))
    if len(uniq) != 1:
        raise ValueError("Unique n not found within bounds.")
    return uniq[0]
