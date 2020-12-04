import copy

start_puzzle_input = [list(line.replace("\n", "")) for line in open('puzzle_input.txt').readlines()]

slope_sizes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

total_trees = []


for slope_size in slope_sizes:
    puzzle_input = copy.deepcopy(start_puzzle_input)
    print(slope_size)
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
    total_trees.append(trees)

total = 1
for t in total_trees:
    total *= t

print(total)