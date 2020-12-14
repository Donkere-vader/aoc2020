from collections import namedtuple

puzzle_input = [line.replace("\n", "") for line in open('puzzle_input.txt').readlines()]

Command = namedtuple("Command", ('mem_loc', 'value'))
Mask = namedtuple("Mask", ('mask'))
commands = []

for line in puzzle_input:
    if line.startswith("mask"):
        mask = line.split("=")[1].strip()
        commands.append(Mask(mask))
    else:
        line = line.replace(" ", "").split("=")
        mem_loc = int(line[0].replace("mem[", "").replace("]", ""))
        value = int(line[1])

        commands.append(Command(mem_loc, value))


class Memory:
    def __init__(self):
        self.mask = ""
        self.__mem = {}

    def set_mem(self, index, value):
        index_mask = self.apply_mask(self.convert_to_byte(index))
        print("index_mask:", index_mask)

        all_mem_locs = self.convert_floating(index_mask)
        for loc in all_mem_locs:
            self.__mem[loc] = self.convert_to_byte(value)

    def convert_to_byte(self, value, min_size=36):
        return "{0:b}".format(value).rjust(min_size, '0')

    def apply_mask(self, value):
        new_string = ""
        for idx, let in enumerate(self.mask):
            if let == "0":
                new_string += value[idx]
            else:
                new_string += let
        return new_string

    def convert_floating(self, value):
        all_outcomes = []
        for i in range(2**value.count("X")):
            temp_val = list(value)
            for bit in self.convert_to_byte(i, min_size=value.count("X")):
                temp_val[temp_val.index("X")] = bit

            all_outcomes.append("".join(temp_val))
        return all_outcomes

    def get_total(self):
        return sum([int(self.__mem[key], 2) for key in self.__mem])

    def output_mem(self):
        for key in self.__mem:
            print(self.__mem[key])


mem = Memory()
for command in commands:
    if type(command).__name__ == "Mask":
        mem.mask = command.mask
    else:
        mem.set_mem(command.mem_loc, command.value)

print(mem.get_total())
