# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

# How many passwords are valid according to their policies?



input = open("input.txt", "r").read()
entries = input.splitlines()

# 9-11 p: pppppppppxblp
number_valid = 0
for entry in entries:
    rule, value = entry.split(':')
    value = value[1:]
    day_range, letter = rule.split(' ')
    lower_bound, upper_bound = [int(x) for x in day_range.split('-')]

    letter_count = {}
    for current_letter in value:
        current_letter_value = letter_count.get(current_letter, 0)
        letter_count[current_letter] = current_letter_value + 1


    if letter in letter_count:
        final_letter_count = letter_count[letter]
        if final_letter_count >= lower_bound and final_letter_count <= upper_bound:
            number_valid += 1

print(number_valid)

