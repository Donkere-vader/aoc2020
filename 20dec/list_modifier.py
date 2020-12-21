
class ListModifierError(Exception):
    pass


def rotate_matrix(matrix, rotation_amount=1):
    """ rotate list 90 degrees clockwise {rotation_amount} times"""
    for _ in range(4-rotation_amount):
        matrix = [
            [matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]) - 1, - 1, - 1)
        ]
    return matrix


def mirror_matrix(matrix, direction="vertical"):
    """ Mirror a list vertical or horizontal """
    if direction == "horizontal":
        return [[i for i in reversed(row)] for row in matrix]
    elif direction == "vertical":
        return [i for i in reversed(matrix)]
    else:
        raise ListModifierError(
            f"Error mirroring list: Invalid direction '{direction}'"
        )


def possible_list_states(matrix):
    yielded_matrixes = []
    for rotation_amount in range(0, 4):
        m = rotate_matrix(matrix, rotation_amount)
        if m not in yielded_matrixes:
            yield m
            yielded_matrixes.append(m)
        for mirror_direction in ['vertical', 'horizontal']:
            m2 = mirror_matrix(m, direction=mirror_direction)
            if m2 not in yielded_matrixes:
                yield m2
                yielded_matrixes.append(m2)


def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))


if __name__ == "__main__":
    import random
    matrix = [[random.randint(0, 1) for _2 in range(3)] for _ in range(3)]

    print_matrix(matrix)

    print("\n---\n")
    for m in possible_list_states(matrix):
        print_matrix(m)
        print()
