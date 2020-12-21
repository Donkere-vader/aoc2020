puzzle_input = [list(line.replace("\n", "")) for line in open('puzzle_input.txt').readlines()]

slope_size = (3, 1)
trees = 0

def print_puzzle(lst):
    for y in lst:
        print("".join(y))

x = 0
for y in range(0, len(puzzle_input), slope_size[1]):
    if puzzle_input[y][x] == "#":
        trees += 1

    puzzle_input[y][x] = 'O' if puzzle_input[y][x] == '.' else 'X'

    x += slope_size[0]
    if x > len(puzzle_input[y]) - 1:
        x -= len(puzzle_input[y])

print_puzzle(puzzle_input)
print(trees)