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


class Ticket:
    def __init__(self, fields, type):
        self.fields = fields
        self.type = type

    def check_fields(self, constraints):
        wrong_fields = []
        for field in self.fields:
            valid = False
            for key in constraints:
                for rnge in constraints[key]:
                    if field >= rnge[0] and field <= rnge[1]:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                wrong_fields.append(field)
        return wrong_fields

    def __repr__(self):
        return f"<{self.type}_ticket {self.fields}>"


print(constraints)

your_ticket = Ticket(your_ticket, "your")
nearby_tickets = [Ticket(n, "nearby") for n in nearby_tickets]

wrong_fields = []
for ticket in nearby_tickets:
    wrong_fields += ticket.check_fields(constraints)

print(wrong_fields)
print(sum(wrong_fields))
