puzzle_input = [list(line.replace("\n", "")) for line in open('puzzle_input.txt').readlines()]


class Cube:
    def __init__(self, parent, x, y, z, active):
        self.parent = parent
        self.x, self.y, self.z = (x, y, z)
        self.active = active
        self.next_state = self.active
        self.updated = False

    def update(self):
        neighbours = self.get_neighbours()

        if self.active and neighbours in (2, 3):
            self.next_state = True
        elif not self.active and neighbours == 3:
            self.next_state = True
        else:
            self.next_state = False

        self.updated = True

    def update_state(self):
        self.active = self.next_state

    def get_neighbours(self):
        neighbours = 0
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if z == 0 and y == 0 and x == 0:
                        continue
                    n = self.parent.get_grid(
                        self.x + x,
                        self.y + y,
                        self.z + z,
                        make_neighbours=self.active
                    )
                    if n is not None and n.active:
                        neighbours += 1
        return neighbours

    def __repr__(self):
        return "#" if self.active else "."

    def rich_repr(self):
        return f"<Cube {repr(self)} @ {(self.x, self.y, self.z)}>"


class Cuber:
    def __init__(self, puzzle_input, loops):
        matrix_3d = [puzzle_input]
        self.grid = {}
        for z_idx, z in enumerate(matrix_3d):
            for y_idx, y in enumerate(z):
                for x_idx, x in enumerate(y):
                    cube = Cube(self, x_idx, y_idx, z_idx, True if x == "#" else False)
                    self.set_grid(x_idx, y_idx, z_idx, cube)

        self.loops = loops

    def set_grid(self, x, y, z, value):
        self.grid[f"{z}:{y}:{x}"] = value

    def get_grid(self, x, y, z, make_neighbours=True):
        idx = f"{z}:{y}:{x}"
        if idx not in self.grid:
            if make_neighbours:
                self.grid[idx] = Cube(self, x, y, z, False)
            else:
                return None
        return self.grid[idx]

    @property
    def cubes(self):
        cubes = []
        for key in self.grid:
            cubes.append(self.grid[key])
        return cubes

    def loop(self):
        for _ in range(self.loops):
            updated_all = False
            while not updated_all:
                for cube in self.cubes:
                    cube.update()

                updated_all = True
                for cube in self.cubes:
                    if not cube.updated:
                        updated_all = False
                        break

            for cube in self.cubes:
                cube.update_state()

        self.result()

    def start(self):
        self.loop()

    def result(self):
        tot = 0
        for cube in self.cubes:
            if cube.active:
                tot += 1
        print(tot)


def main():
    cuber = Cuber(puzzle_input, 6)
    cuber.start()


if __name__ == "__main__":
    main()
