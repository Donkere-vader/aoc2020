from string import ascii_lowercase

puzzle_input = open('puzzle_input.txt').read()
puzzle_input = puzzle_input.split("\n\n")
puzzle_input = [line.replace("\n", "") for line in puzzle_input]

counts = {}

for let in list(ascii_lowercase):
    counts[let] = 0

for let in list(ascii_lowercase):
    for group in puzzle_input:
        if let in group:
            counts[let] += 1

total = 0
for key in counts:
    total += counts[key]

print("Total:", total)