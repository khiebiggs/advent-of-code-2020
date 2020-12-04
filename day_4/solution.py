input_file = open("input.txt", "r").read()

entries = input_file.split('\n\n')
passports = [[y for y in x if y != ''] for x in [x.replace('\n', ' ').split(' ') for x in entries]]

def validate_fields(required, seen, optional):
    difference = required.difference(seen)
    ans = difference.issubset(optional)
    return(ans)

def check_range(value, start, end):
    return value >= start and value <= end

def validate_values(key, value):
    if key == 'cid':
        return True # we don't need to validate this
    if key == 'byr':
        value_as_num = int(value)
        return check_range(value_as_num, 1920, 2002)
    if key == 'iyr':
        value_as_num = int(value)
        return check_range(value_as_num, 2010, 2020)
    if key == 'eyr':
        value_as_num = int(value)
        return check_range(value_as_num, 2020, 2030)
    if key == 'hgt':
        front = value[:-2]
        back = value[-2:]
        if front.isnumeric() and back in ['cm','in']:
            front = int(front)
            if back == 'cm':
                return check_range(front, 150, 193)
            else:
                return check_range(front, 59, 76)
    if key == 'hcl':
        if value[0] == '#':
            count = 0
            valid = True
            for letter in value[1:]:
                count += 1
                valid = letter.isnumeric() or letter in ['a','b','c','d','e','f']
            return valid and len(value[1:]) == 6
    if key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if key == 'pid':
        return len(value) == 9 and value.isnumeric()
    return False


required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
optional = {'cid'}

valid_count = 0

for passport in passports:
    seen = set()
    valid_values = True
    for item in passport:
        key, value = tuple(item.split(':'))
        valid_values = valid_values and validate_values(key, value)
        seen.add(key)
    if valid_values and validate_fields(required, seen, optional):
        valid_count += 1

print(valid_count)
