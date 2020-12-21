inpt = open('x').readlines()

tiles = []
idx = -1

output = ""
for line in inpt:
    idx += 1
    if idx == 0 or idx == 9:
        continue
    if line == "\n":
        idx = -1
        continue

    i = -1
    for c in line:
        i += 1
        if i == 0 or i == 9:
            continue
        elif c == " ":
            i = -1
            continue
        output += c

    output += "\n"

print(output)
