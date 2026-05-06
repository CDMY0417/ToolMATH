def simulate_divisor_removal_game(n: int, first_move: int, policy: str = 'min'):
    'Simulate the divisor-removal game on 1..n with fixed first move.'
    if n < 1:
        raise ValueError('n must be >= 1')
    if first_move < 1 or first_move > n:
        raise ValueError('first_move must be in 1..n')
    remaining = set(range(1, n + 1))

    def has_proper_divisor_in_set(x):
        for d in remaining:
            if d != x and d > 0 and x % d == 0:
                return True
        return False

    def remove_divisors_of(x):
        nonlocal remaining
        to_remove = [d for d in remaining if x % d == 0]
        for d in to_remove:
            remaining.remove(d)
        return to_remove

    if first_move not in remaining or not has_proper_divisor_in_set(first_move):
        raise ValueError('first_move is not a valid Carolyn move')
    carolyn_sum = 0
    paul_sum = 0
    carolyn_moves = []

    remaining.remove(first_move)
    carolyn_moves.append(first_move)
    carolyn_sum += first_move
    for d in remove_divisors_of(first_move):
        paul_sum += d

    while True:
        valid = [x for x in remaining if has_proper_divisor_in_set(x)]
        if not valid:
            paul_sum += sum(remaining)
            remaining.clear()
            break
        if policy == 'min':
            move = min(valid)
        elif policy == 'max':
            move = max(valid)
        else:
            raise ValueError("policy must be 'min' or 'max'")
        remaining.remove(move)
        carolyn_moves.append(move)
        carolyn_sum += move
        for d in remove_divisors_of(move):
            paul_sum += d

    return {
        'carolyn_sum': carolyn_sum,
        'paul_sum': paul_sum,
        'carolyn_moves': carolyn_moves,
    }
