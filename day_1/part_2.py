# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
# In your expense report, what is the product of the three entries that sum to 2020? 


input = open("input.txt", "r").read()
entries = [int(x) for x in input.splitlines()]
entries.sort(reverse=True)

counter = 0 
for i in range(0, len(entries) - 2) :
        first = entries[i]
        j = i + 1
        k = len(entries) - 1
        while( j < k ):
            counter += 1
            second = entries[j]
            third = entries[k]
            total_sum = first + second + third
            if (total_sum) == 2020:
                print(f'found in {counter + 1} tries')
                print(first * second * third)
                quit()
            elif (total_sum) < 2020:
                k -= 1
            elif (total_sum) > 2020:
                j += 1
print('not found')

