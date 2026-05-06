def sequence_periodicity(current_index: int, steps_ahead: int, period: int):
    return (current_index + steps_ahead) % period
