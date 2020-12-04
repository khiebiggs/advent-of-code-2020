# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?


input = open("input.txt", "r").read()
entries = input.splitlines()

ski_map = []
for entry in entries:
    ski_map.append(list(entry))


print(f'i length: {len(ski_map)}')
print(f'j length: {len(ski_map[0])}')

def count_trees_in_slope(slope_map, right_increase, down_increase):
    i, j = 0, 0
    tree_count = 0
    while i < len(slope_map):
        if slope_map[i][j] == '#':
            tree_count += 1
        if j + right_increase >= len(slope_map[i]):
            j = (j + right_increase) - (len(slope_map[i]))  
        else:
            j += right_increase
        i += down_increase

    return tree_count

# (right, down)
instructions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1
for instruction in instructions:
    right_increase, down_increase = instruction
    tree_count = count_trees_in_slope(ski_map, right_increase, down_increase)
    print(f'Right {right_increase}, down {down_increase}: {tree_count}')
    product *= tree_count

print(f'product: {product}')
