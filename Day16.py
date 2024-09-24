def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(N,M):
    return abs(N*M)//gcd(N,M)

print('-----------Test Case 1-----------')
print('Input: N = 4, M = 6')
print(f'Output: {lcm(4, 6)}')
print('-----------Test Case 1-----------')
print('Input: N = 5, M = 10')
print(f'Output: {lcm(5, 10)}')
print('-----------Test Case 1-----------')
print('Input: N = 7, M = 3')
print(f'Output: {lcm(7, 3)}')
print('-----------Test Case 1-----------')
print('Input: N = 1, M = 987654321')
print(f'Output: {lcm(1, 987654321)}')
print('-----------Test Case 1-----------')
print('Input: N = 123456, M = 789012')
print(f'Output: {lcm(123456, 789012)}')
