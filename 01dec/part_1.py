puzzle_input = [int(i) for i in open('puzzle_input.txt').readlines()]

def all_duos(lst):
    for idx, first_num in enumerate(lst):
        for second_num in lst[idx+1:]:
            yield (first_num, second_num)

for duo in all_duos(puzzle_input):
    if sum(duo) == 2020:
        print(f"duo = {duo}")
        break

print(f"{duo[0]} * {duo[1]} = {duo[0] * duo[1]}")
