import copy

puzzle_input = [{"opr" : line.split(" ")[0], "arg": int(line.split(" ")[1].replace("\n", ""))} for line in open('puzzle_input.txt').readlines()]


def generate_sequences(puzzle_input):
    for y in range(len(puzzle_input)):
        sequence = copy.deepcopy(puzzle_input)
        
        if sequence[y]['opr'] == 'acc':
            continue
        elif sequence[y]['opr'] == 'nop':
            sequence[y]['opr'] = 'jmp'
        else:
            sequence[y]['opr'] = 'nop'
        
        sequence[y]['changed'] = True

        yield sequence


for command_sequence in generate_sequences(puzzle_input):
    print()
    acc = 0
    head = 0

    executed_instructions = []
    broke = False
    while True:
        if head not in executed_instructions:
            executed_instructions.append(head)
        else:
            broke = True
            break

        try:
            command = command_sequence[head]
        except IndexError:
            break

        # print(head, command['opr'], command['arg'])

        if command['opr'] == 'acc':
            acc += command['arg']
        if command['opr'] == 'jmp':
            head += command['arg']
        else:
            head += 1

    for idx, command in enumerate(command_sequence):
        indx = ""
        if idx in executed_instructions:
            indx = executed_instructions.index(idx) + 1
        
        print(f"{command['opr']} {command['arg']}".ljust(10), '|', indx, "  CHANGED" if 'changed' in command else "")

    print(broke)
    if not broke:
        print("COMPLETED")
        break

print(acc)
