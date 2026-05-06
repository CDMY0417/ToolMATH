def external_parallelepipeds_volume(length: int, width: int, height: int, external_height: int) -> int:
    return 2 * (length * width * external_height + length * height * external_height + width * height * external_height)
