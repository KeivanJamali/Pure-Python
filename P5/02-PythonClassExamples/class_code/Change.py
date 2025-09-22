def change(total, coins: list):
    dp = [0] * (total + 1)    
    dp[0] = 1    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[total]

print(change(1000, [50, 100, 200, 500]))