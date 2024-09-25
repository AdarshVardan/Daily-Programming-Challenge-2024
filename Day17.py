import math

def prime_factors(num):
    factors=[]
    while num%2==0:
        factors.append(2)
        num//=2
    for i in range(3,int(math.sqrt(num))+1,2):
        while num%i==0:
            factors.append(i)
            num//=i
    if num>2:
        factors.append(num)
    return factors

print('-----------Test Case 1-----------')
print('Input: N = 30')
print(f'Output: {prime_factors(30)}')
print('-----------Test Case 2-----------')
print('Input: N = 49')
print(f'Output: {prime_factors(49)}')
print('-----------Test Case 3-----------')
print('Input: N = 19')
print(f'Output: {prime_factors(19)}')
print('-----------Test Case 4-----------')
print('Input: N = 64')
print(f'Output: {prime_factors(64)}')
print('-----------Test Case 5-----------')
print('Input: N = 123456')
print(f'Output: {prime_factors(123456)}')
