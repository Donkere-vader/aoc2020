puzzle_input = [int(i) for i in open('puzzle_input.txt').readlines()[0].split(",")]


class Memory:
    def __init__(self, starting_numbers: list, t_to_find: int):
        self.t_to_find = t_to_find
        self.starting_numbers = starting_numbers
        self.spoken = {}
        for idx, i in enumerate(self.starting_numbers[:-1]):
            self.spoken[i] = idx  + 1

        self.found_num = None

    def loop(self):
        t = len(self.starting_numbers) + 1
        num = self.starting_numbers[-1]

        while True:
            past_num = num
            if past_num in self.spoken:
                num = t - 1 - self.spoken[past_num]
            else:
                num = 0
    
            if t == self.t_to_find:
                self.found_num = num
                break
            else:
                if t % 100000 == 0:
                    print(t, self.t_to_find - t)

            self.spoken[past_num] = t - 1
            t += 1

    def start(self):
        self.loop()


mem = Memory(puzzle_input, 30000000)
mem.start()
print("------")
print(mem.found_num)
