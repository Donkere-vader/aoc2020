puzzle_input = [line.replace("\n", "") for line in open('puzzle_input.txt').readlines()]

valid = []
invalid = []

def break_down_line(line):
    # break loose password
    split = line.split(":")
    constrains, password = split[0].strip(), split[1].strip()

    # break loose letter
    split = constrains.split(" ")
    occurances, letter = split[0], split[1]

    # get min and max
    split = occurances.split('-')
    possitions = (int(split[0]), int(split[1]))

    return possitions, letter, password

    return occurances, letter, password

for line in puzzle_input:
    possitions, letter, password = break_down_line(line)

    print(possitions, letter, password)

    if (password[possitions[0] - 1] == letter) ^ (password[possitions[1] - 1] == letter):
        valid.append(password)
    else:
        invalid.append(password)


print(valid)
print(invalid)

print(len(valid))
