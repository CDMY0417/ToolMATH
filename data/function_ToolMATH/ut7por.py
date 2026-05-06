def generate_digit_sequence(start_digit: int, common_difference: int, sequence_length: int):
    sequence = []
    current_digit = start_digit
    for _ in range(sequence_length):
        sequence.append(current_digit)
        current_digit = (current_digit + common_difference) % 10
    return sequence
