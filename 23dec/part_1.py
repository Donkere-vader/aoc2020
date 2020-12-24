puzzle_input = [int(cup) for cup in list(open('puzzle_input.txt').readlines()[0])]

print(puzzle_input)


class Game:
    def __init__(self, cups):
        self.cups = cups

    def start(self):
        self.current_cup = self.cups[0]
        self.main_loop()
    
    def print_cups(self):
        print("cups: ", end="")
        for cup in self.cups:
            if cup == self.current_cup:
                print(f"({cup})", end=" ")
            else:
                print(cup, end=" ")
        print()

    def main_loop(self):
        # game has 100 moves
        for move_num in range(100):
            # print some information
            print(f"\n-- move {move_num + 1} --")
            self.print_cups()

            self.destination_cup = None
            self.picked_up = []

            # remove three cups clockwise of current cup
            current_cup_idx = self.cups.index(self.current_cup)
            for i in range(current_cup_idx+1, current_cup_idx+4):
                idx = i
                if idx >= len(self.cups) - 1:
                    idx -= 9
                self.picked_up.append(self.cups[idx])
            for cup in self.picked_up:
                self.cups.remove(cup)
            
            print(f"Picked up: {self.picked_up}")
            
            # select destination cup
            for i in range(1, 9):
                cup_label = self.current_cup - i
                if cup_label < 1:
                    cup_label += 9

                if cup_label in self.cups:
                    self.destination_cup = cup_label
                    break
            
            print(f"Destination cup: {self.destination_cup}")

            # insert back the picked up cups
            destination_cup_idx = self.cups.index(self.destination_cup)
            self.cups = self.cups[:destination_cup_idx+1] + self.picked_up + self.cups[destination_cup_idx+1:]

            # select new current cup
            current_cup_idx = self.cups.index(self.current_cup)
            new_cup_idx = current_cup_idx + 1
            if new_cup_idx >= len(self.cups) - 1:
                new_cup_idx -= 9

            self.current_cup = self.cups[new_cup_idx]

        print("\n-- final --")
        self.print_cups()
    
    def get_answer_string(self):
        idx = self.cups.index(1)
        return "".join(
            [str(i) for i in self.cups[idx+1:] + self.cups[:idx]]
        )
        
        

def main():
    game = Game(puzzle_input)
    game.start()
    print()
    print("Answer:")
    print(game.get_answer_string())


if __name__ == "__main__":
    main()
