puzzle_input = [int(i) for i in open('puzzle_input.txt').readlines()]

def all_duos(lst):
    for idx, first_num in enumerate(lst):
        for second_num in lst[idx+1:]:
            yield (first_num, second_num)

def all_trios(lst):
    for third_num in lst:
        for duo in all_duos(lst):
            if third_num not in duo:
                yield (duo[0], duo[1], third_num)


for trio in all_trios(puzzle_input):
    if sum(trio) == 2020:
        print(f"trio = {trio}")
        break

print(f"{trio[0]} * {trio[1]} * {trio[2]} = {trio[0] * trio[1] * trio[2]}")
