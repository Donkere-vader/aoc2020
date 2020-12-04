# load puzzle input
file_contents = [line.replace("\n", "") for line in open('puzzle_input.txt').readlines()]

passports = []
new_passport = {}
for line in file_contents:
    if len(line) == 0:
        passports.append(new_passport)
        new_passport = {}
        continue

    items = line.split(" ")
    for item in items:
        split = item.split(":")
        new_passport[split[0]] = split[1]

if len(new_passport) > 0:
    passports.append(new_passport)


def validate_field(field, value):
    if field == 'byr':
        value = int(value)
        if value < 1920 or value > 2002:
            return False
    elif field == 'iyr':
        value = int(value)
        if value < 2010 or value > 2020:
            return False
    elif field == 'eyr':
        value = int(value)
        if value < 2020 or value > 2030:
            return False
    elif field == 'hgt':
        if 'cm' in value:
            hgt = int(value.replace('cm', ''))
            if hgt < 150 or hgt > 193:
                return False
        elif 'in' in value:
            hgt = int(value.replace('in', ''))
            if hgt < 59 or hgt > 76:
                return False
        else:
            return False
    elif field == 'hcl':
        if not value.startswith('#'):
            return False
        value = value.replace('#', '')

        allowed_chars = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']

        for let in value:
            if let not in allowed_chars:
                return False
    elif field == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if value not in colors:
            return False
    elif field == 'pid':
        if len(value) != 9:
            return False
    
    return True

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = []

for p in passports:
    valid = True
    for field in required_fields:
        if field not in p or not validate_field(field, p[field]):
            valid = False
            break
    
    if valid:
        valid_passports.append(p)

for p in valid_passports:
    print(p)
    print()

print(len(valid_passports))
