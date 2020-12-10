puzzle_input = sorted([int(line.replace("\n", "")) for line in open('puzzle_input.txt').readlines()])

chain = [0]
for adapter in puzzle_input:
    if adapter - chain[-1] <= 3:
        chain.append(adapter)

# add device
chain.append(chain[-1] + 3)

print(chain)

differences = {
    1: 0,
    2: 0,
    3: 0
}

for idx, adapter in enumerate(chain):
    if idx == 0:
        continue

    differences[adapter - chain[idx - 1]] += 1

print(differences[1], differences[3], differences[1] * differences[3])
