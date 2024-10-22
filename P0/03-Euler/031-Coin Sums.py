coins = [200, 100, 50, 20, 10, 5, 2, 1]
objective = 200
cache = {}
result = 0
def recursive(objective:int, coin_list:list):
    global result
    if objective <= 0:
        return
    if not coin_list:
        return
    max_number = objective//coin_list[0]
    for i in range(max_number, -1, -1):
        if abs(objective - i * coin_list[0]) < 0.01:
            result += 1
            continue
        recursive(objective=objective - i * coin_list[0], coin_list=coin_list[1:])
    return
# recursive(objective=objective, coin_list=coins)
# print(result)

################### Effitient #####################

import numpy as np

# Coefficients for the equation
coefficients = np.array([200, 100, 50, 20, 10, 5, 2, 1])
target_sum = 200
# Create an array to hold the number of ways to make each amount
ways = np.zeros(target_sum + 1, dtype=int)
ways[0] = 1  # There's one way to create the sum of 0 (using no coins)
# # Update ways for each coefficient
for coin in reversed(coefficients):
    for amount in range(coin, target_sum + 1):
        ways[amount] += ways[amount - coin]
# # The number of ways to make the target sum
print(f"Total number of solutions: {ways[target_sum]}")
