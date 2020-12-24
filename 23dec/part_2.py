import os
import time

puzzle_input = [int(cup) for cup in list(open('puzzle_input.txt').readlines()[0])]

print(puzzle_input)

TOTAL_CUPS = 1000000
TOTAL_MOVES = 10000000

class Game:
    def __init__(self, cups):
        self.cups = [i+1 for i in range(TOTAL_CUPS)]
        for idx, cup in enumerate(cups):
            self.cups[idx] = cup
        self.past_cups = self.cups.copy()
        # self.cups = cups


    def start(self):
        self.answers = []
        self.current_cup = self.cups[0]
        self.main_loop()
    
    def beauty_cups(self):
        enormous_string = ""
        for idx in range(50000):
            x = " " if self.cups[idx] > 9 else str(self.cups[idx])
            if self.cups[idx] != self.past_cups[idx]:
                enormous_string += "\u001b[41m" + x
            elif idx+1 == self.cups[idx]:
                enormous_string += "\u001b[41m" + x
            else:
                enormous_string += "\u001b[43m" + x
        enormous_string += "\u001b[0;0;0m"
        print(enormous_string)
        self.past_cups = self.cups.copy()
        time.sleep(0.05)


    def print_cups(self):
        print("cups: ", end="")
        for cup in self.cups:
            if cup == self.current_cup:
                print(f"({cup})", end=" ")
            else:
                print(cup, end=" ")
        print()
    
    def insert_in_cups(self, lst, idx):
        self.cups = self.cups[:idx] + lst + self.cups[idx:]

    def main_loop(self):
        moves = 0
        while True:
            print(moves, TOTAL_CUPS, round((moves / TOTAL_CUPS) * 100, 2), "%", moves - len(self.answers))

            # os.system("clear")
            # self.beauty_cups()
            # print(f"\n-- move {move_num} --")
            # self.print_cups()
            # input()

            self.destination_cup = None
            self.picked_up = []

            # (58, 779)
            current_cup_idx = self.cups.index(self.current_cup)
            # check for ordered part
            # ordered_part = [self.current_cup]
            
            # for i in range(1, TOTAL_CUPS - (current_cup_idx + 1)):
            #     idx = current_cup_idx + i
            #     if self.cups[idx-1] + 1 != self.cups[idx]:
            #         break
            #     ordered_part.append(self.cups[idx])
            
            # if len(ordered_part) >= 4:
            #     ordered_part = ordered_part[: len(ordered_part) - len(ordered_part) % 4]
            #     lst = []
            #     end = [x for x in reversed([self.cups[current_cup_idx-i] for i in range(1, 4)])]
            #     for idx, num in enumerate(ordered_part):
            #         self.cups.remove(num)
            #         if idx % 4 == 0:
            #             end.append(num)
            #             moves += 1
            #         else:
            #             lst.append(num)

            #     lst = lst + end
            #     self.insert_in_cups(lst, current_cup_idx)
            #     self.current_cup = self.cups[current_cup_idx + len(lst)]
            #     continue

            # remove three cups clockwise of current cup
            for i in range(current_cup_idx + 1, current_cup_idx + 4):
                if i >= len(self.cups) - 1:
                    i -= 9
                self.picked_up.append(self.cups[i])
            for cup in self.picked_up:
                self.cups.remove(cup)
            
            # print(f"Picked up: {self.picked_up}")

            # select destination cup
            for i in range(1, TOTAL_CUPS - 1):
                cup_label = self.current_cup - i
                if cup_label < 1:
                    cup_label += 9

                if cup_label in self.cups:
                    self.destination_cup = cup_label
                    break
            
            # print(f"Destination cup: {self.destination_cup}")

            # insert back the picked up cups
            destination_cup_idx = self.cups.index(self.destination_cup)
            self.insert_in_cups(self.picked_up, destination_cup_idx + 1)

            # select new current cup
            current_cup_idx = self.cups.index(self.current_cup)
            new_cup_idx = current_cup_idx + 1
            if new_cup_idx >= len(self.cups) - 1:
                new_cup_idx -= TOTAL_CUPS - 1

            self.current_cup = self.cups[new_cup_idx]
            ans = self.get_answer_string()
            if ans is self.answers:
                print(ans)
            else:
                self.answers.append(ans)

            moves += 1
            if moves == TOTAL_MOVES:
                break
        
        print("\n-- final --")
        self.print_cups()
    
    def get_answer_string(self):
        # idx = self.cups.index(1)
        # return "".join(
        #     [str(i) for i in self.cups[idx+1:] + self.cups[:idx]]
        # )
        idx = self.cups.index(1)
        return self.cups[idx+1], self.cups[idx+2]
        
        

def main():
    game = Game(puzzle_input)
    game.start()
    print()
    print("Answer:")
    print(game.get_answer_string())


if __name__ == "__main__":
    main()
