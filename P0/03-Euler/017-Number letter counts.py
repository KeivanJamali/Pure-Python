"""ONE_DEGREE = one, two, three, four, five, six, seven, eight, nine. 9"""
List_one_degree = [3, 3, 5, 4, 4, 3, 5, 5, 4]
"""TWO_DEGREE = ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen. 10"""
List_two_degree = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
"""TREE_DEGREE = ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety. 9"""
List_tree_degree = [3, 6, 6, 5, 5, 5, 7, 6, 6]
"""FOUR_DEGREE = hundred"""
List_four_degree = [7]

# ___ One to Nine
S_one = 0
count = 0
for i in List_one_degree:
    S_one += i
    count += 1

# ___ ten to nineteen
S_two = 0
for i in List_two_degree:
    S_two += i
    count += 1

# ___ twenty to ninety nine
S_tree = 0
for i in range(1, 9):
    S_tree += List_tree_degree[i]
    count += 1
    for j in List_one_degree:
        S_tree += List_tree_degree[i] + j
        count += 1

big_sum = S_one + S_two + S_tree

# ___ one hundred to nine hundred and ninty_nine
h = 7  # hundred
S_four = 0
count2 = 0
for i in List_one_degree:
    S_four += i + h
    count2 += 1
    S_four += (i + h + 3) * count
    count2 += count
    S_four += big_sum
print(count2)
print(count2+count)
# ___ one thousand
Last_answer = S_four + big_sum + 11
print(Last_answer)
