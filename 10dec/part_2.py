puzzle_input = sorted([int(line.replace("\n", "")) for line in open('puzzle_input.txt').readlines()])

arrangements = 1

chain = [0]

for adapter in puzzle_input:
    new_chain = chain.copy()
    if adapter - chain[-1] <= 3:
        chain.append(adapter)

chain.append(chain[-1] + 3)
print(chain)

class Adapter:
    def __init__(self, value):
        self.value = value
        self.reachable_via = []
        self.steps_to = None

    def __repr__(self):
        return str(self.value)

def d(adapter: Adapter):
    if adapter.steps_to is None:
        adapter.steps_to = max(1, sum([d(a) for a in adapter.reachable_via]))
    return adapter.steps_to

chain = [Adapter(a) for a in chain]

for adapter in chain:
    for a in chain:
        if 0 < adapter.value - a.value <= 3:
            adapter.reachable_via.append(a)

print(chain[-1])
print(d(chain[-1]))
