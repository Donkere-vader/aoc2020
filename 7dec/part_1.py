SEARCHING_COLOR = "shiny gold".replace(" ", "")

puzzle_input = [line.replace("\n", "") for line in open('puzzle_input.txt').readlines()]

# load input
cases = {}
for line in puzzle_input:
    line = line.split(", ")

    color = line[0].split("bags")[0].replace(" ", "")
    
    contain_colors = []

    contain_colors_string = [line[0].split("contain")[1].strip()]
    for bag_color in line[1:] + contain_colors_string:
        bag_color = bag_color[2:].replace("bags", "").replace("bag", "").replace(" ", "").replace(".", "")
        contain_colors.append(bag_color)

    if color in cases:
        cases[color] += contain_colors
    else:
        cases[color] = contain_colors

print("Cases")
for key in cases:
    print(key.ljust(25), cases[key])

print("\n" * 2)

def get_parents(cases, color):
    parents = []
    for key in cases:
        if color in cases[key]:
            parents.append(key)
    return parents


found_all = False
parents = get_parents(cases, SEARCHING_COLOR)
while not found_all:
    found_all = True

    new_parents = []
    for p in parents:
        add_parents = get_parents(cases, p)
        
        for par in add_parents:
            if par == SEARCHING_COLOR or par == "other":
                continue
            elif par not in parents and par not in new_parents:
                new_parents.append(par)
                found_all = False

    parents += new_parents

print("Parents:")
print(parents, len(parents))
