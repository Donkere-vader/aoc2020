passes = [line.replace("\n", "") for line in open('puzzle_input.txt').readlines()]

ROWS_RANGE = (0, 127)
COLUMNS_RANGE = (0, 7)


def narrow_down(lower_char, higher_char, rnge: tuple, boarding_pass):
    bounds = rnge

    for char in boarding_pass:        
        # check if done
        if abs(bounds[1] - bounds[0]) == 1:
            if char == lower_char:
                return bounds[0]
            elif char == higher_char:
                return bounds[1]

        # get new range
        mid = int((bounds[1] - bounds[0]) // 2) + bounds[0]
        if char == lower_char:
            bounds = (bounds[0], mid)
        elif char == higher_char:
            bounds = (mid + 1, bounds[1])


def calculate_id(boarding_pass):
    row = narrow_down("F", "B", ROWS_RANGE, boarding_pass)
    column = narrow_down("L", "R", COLUMNS_RANGE, boarding_pass)
    
    return row * 8 + column, row, column

def print_airplane_matrix(matrix):
    for idx, y in enumerate(matrix):
        print(str(idx).rjust(4), end=" ")
        for idx2, x in enumerate(y):
            if idx2 % 4 == 0 and idx2 != 0:
                print(" ", end="")
            print(x, end="")
        print()

        if idx % 5 == 0 and idx != 0:
            print()

highest_id = 0
airplance_matrix = [["." for _ in range(COLUMNS_RANGE[1] + 1)] for _ in range(ROWS_RANGE[1] + 1)]

for boarding_pass in passes:
    id, row, column = calculate_id(boarding_pass)

    airplance_matrix[row][column] = "X"

    highest_id = max(highest_id, id)

print_airplane_matrix(airplance_matrix)

print()

in_airplane = False
for idx, row in enumerate(airplance_matrix):
    if in_airplane and row.count(".") == 1:
        column = row.index(".")
        print("seat", idx, column, idx * 8 + column)

    if row.count(".") == 0:
        in_airplane = True


print(f"HIGHEST ID:\n{highest_id}")