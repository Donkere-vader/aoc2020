class Instruction:
    def __init__(self, direction, amount):
        self.direction = direction
        self.amount = amount

    def __repr__(self):
        return f"<Instruction {self.direction}{self.amount}>"


class Boat:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = 90

    def move(self, instruction: Instruction):
        print(instruction)

        if instruction.direction == "R":
            self.facing += instruction.amount
        elif instruction.direction == "L":
            self.facing -= instruction.amount

        if self.facing > 270:
            self.facing -= 360
        elif self.facing < 0:
            self.facing += 360

        elif instruction.direction == "N":
            self.y += instruction.amount
        elif instruction.direction == "E":
            self.x += instruction.amount
        elif instruction.direction == "S":
            self.y -= instruction.amount
        elif instruction.direction == "W":
            self.x -= instruction.amount

        elif instruction.direction == "F":
            if self.facing == 0:
                self.y += instruction.amount
            elif self.facing == 90:
                self.x += instruction.amount
            elif self.facing == 180:
                self.y -= instruction.amount
            elif self.facing == 270:
                self.x -= instruction.amount

        print((self.x, self.y))

    @property
    def manhatten_distance(self):
        return abs(self.x) + abs(self.y)


puzzle_input = [Instruction(line[0], int(line[1:])) for line in open('puzzle_input.txt').readlines()]
print(puzzle_input)

boat = Boat()

for instruction in puzzle_input:
    boat.move(instruction)

print(boat.manhatten_distance)
