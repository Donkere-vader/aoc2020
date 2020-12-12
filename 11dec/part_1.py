from copy import deepcopy

puzzle_input = [list(line.replace("\n", "")) for line in open('puzzle_input.txt').readlines()]

print(puzzle_input)


def get_neigbours(grid, x, y):
    neighbours = 0
    for y2 in [0, 1, -1]:
        for x2 in [-1, 1, 0]:
            if y2 == 0 == x2:
                continue
        
            new_y = y + y2
            new_x = x + x2
            if len(grid) > new_y >= 0 and len(grid[y]) > new_x >= 0:
                if grid[new_y][new_x] == '#':
                    neighbours += 1
    return neighbours


def one_round(grid):
    new_grid = deepcopy(grid)
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '.':
                continue

            neighbours = get_neigbours(grid, x, y)
                
            if neighbours == 0:
                new_grid[y][x] = "#"
            elif neighbours >= 4:
                new_grid[y][x] = "L"


    return new_grid


def print_grid(grid):
    print("\n".join(["".join(line) for line in grid]))

print_grid(puzzle_input)
grid = puzzle_input
new_grid = one_round(grid)
while new_grid != grid:
    grid = deepcopy(new_grid)
    new_grid = one_round(grid)

print()
print_grid(new_grid)
print(sum([line.count("#") for line in new_grid]))
