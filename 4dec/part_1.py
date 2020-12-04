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



required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = []

for p in passports:
    valid = True
    for field in required_fields:
        if field not in p:
            valid = False
            break
    
    if valid:
        valid_passports.append(p)

for p in valid_passports:
    print(p)
    print()

print(len(valid_passports))
