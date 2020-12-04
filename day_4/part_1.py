input = r'''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''

input = open("input.txt", "r").read()
entries = input.split('\n\n')
passports = [[y for y in x if y != ''] for x in [x.replace('\n', ' ').split(' ') for x in entries]]

def validate_fields(required, seen, optional):
    difference = required.difference(seen)
    ans = difference.issubset(optional)
    return(ans)

def validate_values(key, value):
        if key == 'byr':
            value_as_num = int(value)
            return value_as_num >= 1920 and value_as_num <= 2002
        if key == 'iyr':
            value_as_num = int(value)
            return value_as_num >= 2010 and value_as_num <= 2020
        if key == 'eyr':
            value_as_num = int(value)
            return value_as_num >= 2020 and value_as_num <= 2030
        if key == 'hgt':
            front = value[:-2]
            back = value[-2:]
            if front.isnumeric() and back in ['cm','in']:
                front = int(front)
                if back == 'cm':
                    return front >= 150 and front <= 193
                else:
                    return front >= 59 and front <= 76
        if key == 'hcl':
            if value[0] == '#':
                count = 0
                valid = True
                for letter in value[1:]:
                    count += 1
                    valid = letter.isnumeric() or letter in ['a','b','c','d','e','f']
                return valid
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
        valid_values = validate_values(key, value)
        seen.add(key)
    if valid_values and validate_fields(required, seen, optional):
        valid_count += 1

print(valid_count)
# 136 is too high        

# print('byr valid:   2002')
# print(validate_values('byr', '2002'))
# print('byr invalid: 2003')
# print(validate_values('byr', '2003'))

# print('hgt valid:   60in')
# print(validate_values('hgt', '60in'))
# print('hgt valid:   190cm')
# print(validate_values('hgt', '190cm'))
# print('hgt invalid: 190in')
# print(validate_values('hgt', '190in'))
# print('hgt invalid: 190')
# print(validate_values('hgt', '190'))

# print('hcl valid:   #123abc')
# print(validate_values('hcl', '#123abc'))
# print('hcl invalid: #123abz')
# print(validate_values('hcl', '#123abz'))
# print('hcl invalid: 123abc')
# print(validate_values('hcl', '123abc'))

# print('ecl valid:   brn')
# print(validate_values('ecl', 'brn'))
# print('ecl invalid: wat')
# print(validate_values('ecl', 'wat'))

# print('pid valid:   000000001')
# print(validate_values('pid', '000000001'))
# print('pid invalid: 0123456789')
# print(validate_values('pid', '0123456789'))
