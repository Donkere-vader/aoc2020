class Instruction:
    def __init__(self, direction, amount):
        self.direction = direction
        self.amount = amount

    def __repr__(self):
        return f"<Instruction {self.direction}{self.amount}>"


class WayPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent_boat = None

    def move(self, instruction: Instruction):
        print()
        print(self, instruction)
        if instruction.direction == "N":
            self.y += instruction.amount
        elif instruction.direction == "E":
            self.x += instruction.amount
        elif instruction.direction == "S":
            self.y -= instruction.amount
        elif instruction.direction == "W":
            self.x -= instruction.amount

        if instruction.direction in ["R", "L"]:
            for _ in range(instruction.amount // 90):
                delta_x = self.x - self.parent_boat.x  # 10 e
                delta_y = self.y - self.parent_boat.y  # 4 n

                if instruction.direction == "R":
                    self.x = self.parent_boat.x + delta_y
                    self.y = self.parent_boat.y - delta_x
                elif instruction.direction == "L":
                    self.x = self.parent_boat.x - delta_y
                    self.y = self.parent_boat.y + delta_x

        print((self.x, self.y), (self.x - self.parent_boat.x, self.y - self.parent_boat.y))

    def __repr__(self):
        return f"<WayPoint {(self.x, self.y)} {(self.x - self.parent_boat.x, self.y - self.parent_boat.y)}>"


class Boat:
    def __init__(self, way_point: WayPoint):
        self.x = 0
        self.y = 0
        self.facing = 90
        self.way_point = way_point
        self.way_point.parent_boat = self

    def move(self, instruction: Instruction):
        print()
        print(self, instruction)

        if instruction.direction == "F":
            delta_x = self.way_point.x - self.x
            delta_y = self.way_point.y - self.y
            self.x += delta_x * instruction.amount
            self.y += delta_y * instruction.amount
            self.way_point.x += delta_x * instruction.amount
            self.way_point.y += delta_y * instruction.amount

        print((self.x, self.y))

    @property
    def manhatten_distance(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f"<Boat {(self.x, self.y)}>"


puzzle_input = [Instruction(line[0], int(line[1:])) for line in open('puzzle_input.txt').readlines()]
print(puzzle_input)

way_point = WayPoint(10, 1)
boat = Boat(way_point)

for instruction in puzzle_input:
    if instruction.direction == "F":
        boat.move(instruction)
    else:
        boat.way_point.move(instruction)

print(boat.manhatten_distance)
