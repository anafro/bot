from collections import deque


def get_value_by_dot_key(dictionary: dict, dot_key: str):
    key_sequence = deque(dot_key.split('.'))
    current_value = dictionary

    while len(key_sequence) != 0:
        next_key = key_sequence.popleft()

        if current_value is None or next_key not in current_value:
            return None

        current_value = current_value[next_key]

    return current_value