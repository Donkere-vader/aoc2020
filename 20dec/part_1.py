import math
from list_modifier import rotate_matrix, possible_list_states
import os

# load data
puzzle_input = [tile for tile in open('puzzle_input.txt').read().split("\n\n")]

tiles = {}

for tile in puzzle_input:
    tile = tile.split("\n")
    tile_id = int(tile[0].replace("Tile ", "").replace(":", ""))
    del tile[0]
    tiles[tile_id] = [list(row) for row in tile]


class Assembler:
    def __init__(self, tiles):
        self.tiles = tiles
        self.tile_keys = [key for key in tiles]
        self.tile_ids = None

    def print_tile_ids(self, tile_ids):
        for row in tile_ids:
            print(
                " ".join([
                    str(i) if i is not None else "?".ljust(4) for i in row
                ])
            )

    def print_grid(self, grid):
        for row in grid:
            for y in range(10):
                for tile in row:
                    if tile is not None:
                        print("".join([str(i) for i in tile[y]]), end=" ")
                    else:
                        print("?" * 10, end=" ")
                print()
            print()

    def check_tile(self, grid, tile: tuple):
        """ Check if the tile fits the grid"""
        valid = True

        x, y = tile
        tile = grid[y][x]

        top_row = tile[0]
        bottom_row = tile[-1]
        right_column = rotate_matrix(tile)[-1]
        left_column = rotate_matrix(tile)[0]

        # check top neighbour
        if y-1 >= 0:
            top_neighbour = grid[y-1][x]
            if top_neighbour is not None:
                top_neighbour_bottom_row = top_neighbour[-1]
                if top_row != top_neighbour_bottom_row:
                    valid = False

        # check bottom neighbour
        if valid and y+1 < len(grid):
            bottom_neighbour = grid[y+1][x]
            if bottom_neighbour is not None:
                bottom_neighbour_top_row = bottom_neighbour[0]
                if bottom_row != bottom_neighbour_top_row:
                    valid = False

        # check right neigbour
        if valid and x+1 < len(grid):
            right_neighbour = grid[y][x+1]
            if right_neighbour is not None:
                right_neighbour_left_column = rotate_matrix(
                    right_neighbour
                )[0]
                if right_column != right_neighbour_left_column:
                    valid = False

        # check left neighbour
        if valid and x-1 >= 0:
            left_neighbour = grid[y][x-1]
            if left_neighbour is not None:
                left_neighbour_right_column = rotate_matrix(
                    left_neighbour
                )[-1]
                if left_column != left_neighbour_right_column:
                    valid = False

        return valid

    def recursive_checking(self, grid, tile_ids):
        empty_cord = ()
        used_tiles = []
        for y in range(len(grid)):
            for x in range(len(grid)):
                if grid[y][x] is None:
                    empty_cord = (x, y)
                    break
                else:
                    used_tiles.append(tile_ids[y][x])
            if empty_cord:
                break

        if not empty_cord:
            self.tile_ids = [[i for i in row] for row in tile_ids]
            self.grid = grid
            return True

        # Terminal output
        os.system('clear')
        self.print_tile_ids(tile_ids)
        if tile_ids[0][0] is not None:
            print(
                self.tile_keys.index(tile_ids[0][0]),
                "/",
                len(self.tile_keys)
            )

        for tile_id in self.tiles:
            if tile_id in used_tiles:
                continue
            tile = self.tiles[tile_id]

            for t in possible_list_states(tile):
                grid[empty_cord[1]][empty_cord[0]] = t
                tile_ids[empty_cord[1]][empty_cord[0]] = tile_id

                if self.check_tile(grid, empty_cord):
                    if self.recursive_checking(grid, tile_ids):
                        return True

                grid[empty_cord[1]][empty_cord[0]] = None
                tile_ids[empty_cord[1]][empty_cord[0]] = None

    def start(self):
        print("... setting lists")
        grid = [
            [None for _2 in range(int(math.sqrt(len(tiles))))]
            for _ in range(int(math.sqrt(len(tiles))))
            ]
        tile_ids = [
            [None for _2 in range(int(math.sqrt(len(tiles))))]
            for _ in range(int(math.sqrt(len(tiles))))
            ]
        print("... starting loop")
        self.recursive_checking(grid, tile_ids)


def main():
    assembler = Assembler(tiles)
    assembler.start()
    print(assembler.tile_ids)

    print()
    for row in assembler.tile_ids:
        print(" ".join([str(num) for num in row]))
    print()

    multiplied_ids = 1
    for y in [0, -1]:
        for x in [0, -1]:
            multiplied_ids *= assembler.tile_ids[y][x]

    print(multiplied_ids)

    assembler.print_grid(assembler.grid)


if __name__ == "__main__":
    main()
