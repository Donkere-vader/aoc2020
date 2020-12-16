puzzle_input = [line.strip() for line in open('puzzle_input.txt').readlines() if line.strip() != ""]

# loading puzzle input
constraints = {}
nearby_tickets = []

checking = 'constraints'

for line in puzzle_input:
    if line == "your ticket:":
        checking = 'your_ticket'
        continue
    elif line == "nearby tickets:":
        checking = 'nearby_tickets'
        continue

    if checking == "constraints":
        line = line.split(":")
        name = line[0]

        ranges = line[1].replace(" ", "").split("or")
        ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]
        constraints[name] = ranges

    if checking == "your_ticket":
        your_ticket = [int(i) for i in line.split(",")]
    elif checking == "nearby_tickets":
        nearby_tickets.append([int(i) for i in line.split(",")])


def check_constraints(value, constraints):
    valid = False
    for key in constraints:
        for rnge in constraints[key]:
            if value >= rnge[0] and value <= rnge[1]:
                valid = True
                break
        if valid:
            break
    return valid


class Ticket:
    def __init__(self, fields, type):
        self.fields = fields
        self.type = type

    def check_fields(self, constraints):
        wrong_fields = []
        for field in self.fields:
            valid = check_constraints(field, constraints)
            if not valid:
                wrong_fields.append(field)
        return wrong_fields

    def __repr__(self):
        return f"<{self.type}_ticket {self.fields}>"


your_ticket = Ticket(your_ticket, "your")
nearby_tickets = [Ticket(n, "nearby") for n in nearby_tickets]

wrong_tickets = []
for ticket in nearby_tickets:
    wrong_fields = ticket.check_fields(constraints)
    if len(wrong_fields) > 0:
        wrong_tickets.append(ticket)

for ticket in wrong_tickets:
    nearby_tickets.remove(ticket)
del wrong_tickets


def check_column(column, constraints):
    possible_columns = []
    for key in constraints:
        valid = True
        for num in column:
            valid_num = False
            for rnge in constraints[key]:
                if num >= rnge[0] and num <= rnge[1]:
                    valid_num = True
                    break
            if not valid_num:
                valid = False
                break
        if valid:
            possible_columns.append(key)
    return possible_columns


# construct columns
columns = [[] for i in range(len(your_ticket.fields))]
for ticket in nearby_tickets:
    for idx, field in enumerate(ticket.fields):
        columns[idx].append(field)


for idx, column in enumerate(columns):
    possible_field_names = check_column(column, constraints)
    columns[idx] = {
        "fields": column,
        "names": possible_field_names
    }


field_names = ["" for _ in range(len(columns))]
taken_names = []

while "" in field_names:
    for idx, column in enumerate(columns):
        if len(column['names']) == 1:
            taken_names.append(column['names'][0])
            field_names[idx] = column['names'][0]

    for idx, column in enumerate(columns):
        for name in taken_names:
            if name in column['names']:
                column['names'].remove(name)
        columns[idx] = column

departure_nums = []
for name, num in zip(field_names, your_ticket.fields):
    print(f"{name}:".ljust(20), num)
    if name.startswith('departure'):
        departure_nums.append(num)

tot = 1
for num in departure_nums:
    tot *= num
print(tot)
