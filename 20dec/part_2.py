from list_modifier import possible_list_states


puzzle_input = open('puzzle_input.txt').read().split("\n\n")

pattern = [list(line) for line in puzzle_input[0].split("\n")]
matrix = [list(line) for line in puzzle_input[1].split("\n")]


class Searcher:
    def __init__(self, matrix):
        self.matrix = matrix

    @property
    def water_roughness(self):
        tot = 0
        for row in self.matrix:
            tot += row.count("#")
        return tot

    def print_matrix(self, matrix):
        for row in matrix:
            print("".join(row))

    def hashtags(self, matrix):
        cords = []
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == "#":
                    cords.append((x, y))
        return cords

    def detect_on(self, matrix, x, y):
        all_hashtags = True
        translations = [
            (pos[0] + x, pos[1] + y) for pos in self.pattern_hashtags
        ]

        for pos in translations:
            if matrix[pos[1]][pos[0]] != "#":
                all_hashtags = False
                break

        return all_hashtags, translations

    def search(self, pattern):
        self.pattern_hashtags = self.hashtags(pattern)
        self.pattern_dimensions = (len(pattern[0]), len(pattern))

        most_patterns = {
            "most": 0
        }

        for m in possible_list_states(self.matrix):
            patterns = 0

            for y in range(len(m) - self.pattern_dimensions[1] + 1):
                for x in range(
                    len(m[y]) - self.pattern_dimensions[0] + 1
                ):
                    valid, translations = self.detect_on(m, x, y)
                    if valid:
                        patterns += 1
                        for pos in translations:
                            m[pos[1]][pos[0]] = "O"

            if patterns > most_patterns['most']:
                most_patterns = {
                    "most": patterns,
                    "matrix": m
                }

        self.matrix = most_patterns['matrix']
        return most_patterns['most']


def main():
    searcher = Searcher(matrix)
    print(searcher.search(pattern))

    print(searcher.water_roughness)


if __name__ == "__main__":
    main()
