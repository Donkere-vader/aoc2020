puzzle_input = [{"opr" : line.split(" ")[0], "arg": int(line.split(" ")[1].replace("\n", ""))} for line in open('puzzle_input.txt').readlines()]

acc = 0
head = 0

executed_instructions = []

while True:
    if head not in executed_instructions:
        executed_instructions.append(head)
    else:
        break

    command = puzzle_input[head]

    print(head, command['opr'], command['arg'])

    if command['opr'] == 'acc':
        acc += command['arg']
    if command['opr'] == 'jmp':
        head += command['arg']
    else:
        head += 1

print(acc)
