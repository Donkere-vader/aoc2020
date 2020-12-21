from string import ascii_lowercase

puzzle_input = open('puzzle_input.txt').read()
puzzle_input = puzzle_input.split("\n\n")
puzzle_input = [line.split("\n") for line in puzzle_input]

print(puzzle_input)

counts = {}

for let in list(ascii_lowercase):
    counts[let] = 0

for group in puzzle_input:
    for let in group[0]:
        everyone = True
        for person in group[1:]:
            if let not in person:
                everyone = False
                break
        if everyone:
            counts[let] += 1

total = 0
for key in counts:
    total += counts[key]

print("Total:", total)