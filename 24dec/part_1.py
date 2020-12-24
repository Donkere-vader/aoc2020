puzzle_input = [line.strip() for line in open('puzzle_input.txt').readlines()]


class Floor:
    def __init__(self):
        self.black_tiles = []
    
    def strip_order(self, order):
        # load into list
        o = []
        string = ""
        for char in order:
            if char == "w" or char == "e":
                string += char
                o.append(string)
                string = ""
            elif char == "s" or char == "n":
                string += char
        
        print(o)

        y = 0
        x = 0
        for direction in o:
            if "n" in direction:
                y += 1
            elif "s" in direction:
                y -= 1
            
            if "w" in direction and ("n" in direction or "s" in direction):
                x -= 0.5
            elif "w" in direction:
                x -= 1
            elif "e" in direction and ("n" in direction or "s" in direction):
                x += 0.5
            elif "e" in direction:
                x += 1

        return (x, y)

    def flip_tiles(self, orders):
        for order in orders:
            order = self.strip_order(order)
            if order not in self.black_tiles:
                self.black_tiles.append(order)
            else:
                self.black_tiles.remove(order)

def main():
    floor = Floor()
    floor.flip_tiles(puzzle_input)

    print(floor.black_tiles)
    print(len(floor.black_tiles))


if __name__ == "__main__":
    main()
