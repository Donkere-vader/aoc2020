from datetime import datetime as dt


def product(lst):
    tot = 1
    for i in lst:
        tot *= i
    return tot


start_time = dt.now()
puzzle_input = open('puzzle_input.txt').readlines()

earliest_time = int(puzzle_input[0])
busses = [int(bus) if bus != "x" else bus for bus in puzzle_input[1].split(",")]

print(busses)

t = 0
found = False
together = [busses[0]]
while True:
    print(t)
    found = True
    for idx, bus in enumerate(busses):
        if bus == "x":
            continue
        elif (t + idx) % bus != 0:
            found = False
            break
        else:
            if bus not in together:
                together.append(bus)

    if found:
        print(t)
        break

    t += product(together)
