def coinChange(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i]=min(dp[i],dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

print('-----------Test Case 1-----------')
print(f'Input: coins = [1, 2, 5], amount = 11')
print(f'Output: {coinChange([1, 2, 5],11)}')
print('-----------Test Case 2-----------')
print(f'Input: coins = [2], amount = 3')
print(f'Output: {coinChange([2],3)}')
print('-----------Test Case 3-----------')
print(f'Input: coins = [1], amount = 0')
print(f'Output: {coinChange([1],0)}')
