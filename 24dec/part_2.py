puzzle_input = [line.strip() for line in open('puzzle_input.txt').readlines()]

DAYS = 100

class Floor:
    def __init__(self):
        self.black_tiles = []
    
    def get_direction(self, direction):
        x = 0
        y = 0
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

        y = 0
        x = 0
        for direction in o:
            i = self.get_direction(direction)
            x += i[0]
            y += i[1]

        return (x, y)

    def load_tiles(self, orders):
        for order in orders:
            order = self.strip_order(order)
            if order not in self.black_tiles:
                self.black_tiles.append(order)
            else:
                self.black_tiles.remove(order)
    
    def main_loop(self):
        for day in range(DAYS):
            new_tiles = []
            white_tiles = {}

            for tile in self.black_tiles:
                neighbours = 0
                for direction in ["nw", "ne", "sw", "se", "e", "w"]:
                    i = self.get_direction(direction)
                    x = tile[0] + i[0]
                    y = tile[1] + i[1]

                    if (x, y) in self.black_tiles:
                        neighbours += 1
                    
                    if (x, y) in white_tiles:
                        white_tiles[(x, y)] += 1
                    else:
                        white_tiles[(x, y)] = 1
                
                alive = True
                if neighbours == 0 or neighbours > 2:
                    alive = False
                
 
                if alive:
                    new_tiles.append(tile)

            for white_tile in white_tiles:
                if white_tiles[white_tile] == 2 and white_tile not in self.black_tiles:
                    new_tiles.append(white_tile)
            
            
            self.black_tiles = new_tiles
            
            print(f"Day {day + 1}: {len(self.black_tiles)}")

def main():
    floor = Floor()
    floor.load_tiles(puzzle_input)

    print(floor.black_tiles)
    print(len(floor.black_tiles))

    floor.main_loop()
    print(len(floor.black_tiles))


if __name__ == "__main__":
    main()
