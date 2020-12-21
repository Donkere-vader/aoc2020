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

highest_id = 0

for boarding_pass in passes:
    id, row, column = calculate_id(boarding_pass)
    highest_id = max(highest_id, id)

print(f"\nHIGHEST ID:\n{highest_id}")