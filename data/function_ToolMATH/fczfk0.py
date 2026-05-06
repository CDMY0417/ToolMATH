def sum_adjacent_in_row(current_row: list):
    return [current_row[i] + current_row[i + 1] for i in range(len(current_row) - 1)]
