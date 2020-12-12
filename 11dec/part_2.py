from copy import deepcopy
import math

puzzle_input = [list(line.replace("\n", "")) for line in open('puzzle_input.txt').readlines()]

def get_degrees_to(pos1, pos2):
    delta_x = pos2[0] - pos1[0]
    delta_y = pos2[1] - pos1[1]

    degrees = 0.0
    if delta_x < 0:
        degrees += 180
    elif delta_x <= 0 and delta_y > 0:
        degrees += 180
    if delta_y >= 0 and delta_x > 0:
        degrees += 90
    elif delta_y <= 0 and delta_x < 0:
        degrees += 90

    try:
        degrees += abs(math.degrees(math.atan(delta_y / delta_x)))
    except ZeroDivisionError:
        pass

    return degrees


def get_distance(pos1, pos2):
    delta_x = abs(pos1[0] - pos2[0])
    delta_y = abs(pos1[1] - pos2[1])
    return math.sqrt(delta_x**2 + delta_y**2)


def get_neigbours(grid, x, y):
    sees_seats = {}

    for y2 in range(len(grid)):
        for x2 in range(len(grid[y2])):
            if grid[y2][x2].symbol == '.' or (y2 == y and x2 == x):
                continue
            delta_x = x - x2
            delta_y = y - y2
            if abs(delta_x) == abs(delta_y) or y2 == y or x2 == x:
                angle = get_degrees_to((x, y), (x2, y2))
                d = get_distance((x, y), (x2, y2))
                if angle not in sees_seats or sees_seats[angle]['distance'] > d:
                    sees_seats[angle] = {
                        "place": grid[y2][x2],
                        "distance": d
                    }

    return sees_seats


class Place:
    def __init__(self, symbol, x, y):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.next_symbol = symbol
        self.neighbours = []
    
    def get_neigbours(self):
        n = 0

        for neighbour in self.neighbours:
            if neighbour.symbol == "#":
                n += 1
        
        return n

    def __repr__(self):
        return f"<Seat {self.symbol} @ {(self.x, self.y)}>"


def one_round(grid):
    changes = False
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].symbol == '.':
                continue

            neighbours = grid[y][x].get_neigbours()
            # print((x, y), neighbours, grid[y][x].neighbours)
            if neighbours == 0:
                grid[y][x].next_symbol = "#"
            elif neighbours >= 5:
                grid[y][x].next_symbol = "L"

    for row in grid:
        for item in row:
            if item.symbol != item.next_symbol:
                item.symbol = item.next_symbol
                changes = True

    return grid, changes


def print_grid(grid):
    print("\n".join(["".join([i.symbol for i in line]) for line in grid]))

print("Converting puzzle input")
puzzle_input = [[Place(symb, x, y) for x, symb in enumerate(line)] for y, line in enumerate(puzzle_input)]

print("setting neigbours")
# set neighbours
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        neighbours = get_neigbours(puzzle_input, x, y)
        i = [neighbours[n]['place'] for n in neighbours]
        puzzle_input[y][x].neighbours = i

print("Starting rounds")
grid = puzzle_input
while True:
    grid, changes = one_round(grid)

    if not changes:
        break

    print_grid(grid)
    print()


print()
print_grid(grid)

tot = 0
for row in grid:
    for seat in row:
        if seat.symbol == "#":
            tot += 1

print(tot)
