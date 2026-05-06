def probability_same_face(num_faces: int, num_dice: int):
    if num_dice < 1:
        return 0
    first_die_probability = 1  # Since any face can be on the first die
    same_face_probability = (1 / num_faces) ** (num_dice - 1)
    return first_die_probability * same_face_probability
