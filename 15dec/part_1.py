puzzle_input = [int(i) for i in open('puzzle_input.txt').readlines()[0].split(",")]


class Memory:
    def __init__(self, starting_numbers: list):
        self.starting_numbers = starting_numbers
        self.spoken = self.starting_numbers
        self.spoken.reverse()

    def loop(self):
        while True:
            past_num = self.spoken[0]
            print(f"[+] past_num: {past_num}".ljust(20), end=" ")
            print(f"| spoken.count: {self.spoken.count(past_num)}".ljust(20), end=" ")
            if self.spoken.count(past_num) > 1:
                num = self.spoken[1:].index(past_num) + 1
            else:
                num = 0
            print(f"| num: {num}")
            self.spoken.insert(0, num)

            if len(self.spoken) == 2020:
                break

    def start(self):
        self.loop()


mem = Memory(puzzle_input)
mem.start()
# print(mem.spoken)
print(mem.spoken[0])
