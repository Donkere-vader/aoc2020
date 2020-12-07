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
        try:
            bag_amount = int(bag_color.split(" ")[0])
        except ValueError:
            bag_amount = 0

        bag_color = bag_color[2:].replace("bags", "").replace("bag", "").replace(" ", "").replace(".", "")
        contain_colors.append({
            "color": bag_color,
            "amount": bag_amount
        })

    if color in cases:
        cases[color] += contain_colors
    else:
        cases[color] = contain_colors

print("Cases")
for key in cases:
    print(key.ljust(25), cases[key])

print("\n" * 2)

class Batch:
    def __init__(self, color, amount):
        self.color = color
        self.parent = None
        self.children = []
        self.amount = amount
    
    def set_parent(self, parent):
        self.parent = parent
        parent.children.append(self)
    
    def __repr__(self):
        return f"<{self.color} batch of {self.amount}>"

root_batch = Batch(SEARCHING_COLOR, 1)

children = [Batch(child['color'], child['amount']) for child in cases[SEARCHING_COLOR]]
for child in children:
    child.set_parent(root_batch)


found_all = False
while not found_all:
    found_all = True
    new_children = []

    for child in children:
        add_children = [Batch(c['color'], c['amount']) for c in cases[child.color]]
        print(child, add_children)

        for c in add_children:
            if c.color == 'other':
                continue
            already_calculated = False
            for c2 in child.children:
                if c2.color == c.color:
                    already_calculated = True
                    break
        
            if not already_calculated:
                c.set_parent(child)
                new_children.append(c)
                found_all = False

    children += new_children

print()

def add_child(child):
    amount = child.amount
    for c in child.children:
        amount += add_child(c) * child.amount
    return amount

def print_child(child, tabs):
    print(" " * 4 * tabs, end="")
    print(f"{child.amount}x {child.color}")

    for c in child.children:
        print_child(c, tabs + 1)


print(children)
print(add_child(root_batch) - 1)

print_child(root_batch, 0)
