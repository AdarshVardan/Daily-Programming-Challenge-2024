def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1

    dp=[0]*(n+1)
    dp[0],dp[1]=0,1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

print('-----------Test Case 1-----------')
print(f'Input: {5}')
print(f'Output: {fibonacci(5)}')
print('-----------Test Case 2-----------')
print(f'Input: {10}')
print(f'Output: {fibonacci(10)}')
print('-----------Test Case 3-----------')
print(f'Input: {0}')
print(f'Output: {fibonacci(0)}')
print('-----------Test Case 4-----------')
print(f'Input: {1000}')
print(f'Output: {fibonacci(1000)}')
