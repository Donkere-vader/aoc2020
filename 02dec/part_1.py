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
    allowed_amount = (int(split[0]), int(split[1]))

    return allowed_amount, letter, password

    return occurances, letter, password

for line in puzzle_input:
    allowed_amount, letter, password = break_down_line(line)
    
    count = password.count(letter)

    if count >= allowed_amount[0] and count <= allowed_amount[1]:
        valid.append(password)
    else:
        invalid.append(password)


print(valid)
print(invalid)

print(len(valid))
