from string import ascii_lowercase
from datetime import datetime as dt


# load input
lines = [line.strip() for line in open('puzzle_input.txt').readlines()]

rules = {}
messages = []
adding_to = 'rules'
for line in lines:
    if line == "":
        adding_to = 'messages'
    elif adding_to == 'rules':
        line = [i.strip().replace('"', '') for i in line.split(":")]
        if line[1] in ascii_lowercase:
            rule = line[1]
        else:
            rule = [[int(i) for i in rule_set.strip().split(" ")] for rule_set in line[1].split("|")]
        rules[int(line[0])] = rule
    elif adding_to == 'messages':
        messages.append(line)


class Rule:
    def __init__(self, id):
        self.id = id
        self.rules = []
        self.accepted = []

    @property
    def type(self):
        if type(self.rules[0]) == str:
            return 'char'
        return 'masterrule'

    @property
    def char(self):
        return self.rules[0]

    def complies(self, string):
        if self.type == 'char':
            if string.startswith(self.char):
                return True, string[1:]
            return False, string[1:]
        else:
            if self.accepted and string[:len(self.accepted[0])] in self.accepted:
                return True, string[len(self.accepted[0]):]

            comp = False
            for sub_lst in self.rules:
                c = True
                s = string
                for r in sub_lst:
                    c, s = r.complies(s)
                    if not c:
                        break
                if c:
                    comp = True
                    break
                else:
                    print(c, s)

            if comp:
                cut = string[:-len(s)]
                if cut not in self.accepted and cut != "":
                    self.accepted.append(cut)

            return comp, s

    def validate(self, string):
        valid, string = self.complies(string)
        if len(string) > 0:
            valid = False
        return valid

    def __repr__(self):
        if self.type == 'char':
            rule_str = self.rules[0]
        else:
            rule_str = " | ".join([" ".join([str(j.id) for j in i]) for i in self.rules])
        return f"<Rule {self.id} -> {rule_str}>"


class Validator:
    def __init__(self, rules):
        self.load_rules(rules)

    def load_rules(self, rules):
        all_rules = {}
        for r in rules:
            all_rules[r] = Rule(r)

        for r in rules:
            if type(rules[r]) == str:
                all_rules[r].rules.append(rules[r])
            else:
                rules_lst = []
                for sub_list in rules[r]:
                    rules_lst.append(
                        [all_rules[rl] for rl in sub_list]
                    )
                all_rules[r].rules = rules_lst

        self.rules = all_rules

    @property
    def root_rule(self):
        return self.rules[0]

    def validate(self, message):
        return self.root_rule.validate(message)


def main():
    validator = Validator(rules)

    start_time = dt.now()
    valid_messages = []
    for message in messages:
        valid = validator.validate(message)
        if valid:
            valid_messages.append(message)
        print(f"{message} {valid}")
    print("time elapsed:", dt.now() - start_time)

    print('\n == VALID MESSAGES: == ')
    for m in valid_messages:
        print(m)

    print(len(valid_messages))


if __name__ == "__main__":
    main()
