def ones_digit_of_power_a(base: int, exponent: int) -> int:
    digit_cycle = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    cycle = digit_cycle[base % 10]
    cycle_length = len(cycle)
    return cycle[(exponent % cycle_length) - 1]
