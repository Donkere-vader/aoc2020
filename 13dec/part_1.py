puzzle_input = open('puzzle_input.txt').readlines()

earliest_time = int(puzzle_input[0])
busses = [int(bus) for bus in puzzle_input[1].split(",") if bus != "x"]


i = earliest_time - 1
found = False
while not found:
    i += 1
    for bus in busses:
        print(i, bus, i % bus)
        if i % bus == 0:
            found = True
            break

print(bus, i)
print((i - earliest_time) * bus)
