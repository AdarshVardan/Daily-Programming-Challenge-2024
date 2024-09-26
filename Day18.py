import math
def divisors_count(num):
    count=0
    if math.sqrt(num)==int(math.sqrt(num)):
        count=-1
    for i in range(1,int(math.sqrt(num)+1)):
        if num%i==0:
            count+=2
    return count

print('-----------Test Case 1-----------')
print('Input:  N = 18')
print(f'Output: {divisors_count(18)}')
print('-----------Test Case 2-----------')
print('Input:  N = 29')
print(f'Output: {divisors_count(29)}')
print('-----------Test Case 3-----------')
print('Input:  N = 100')
print(f'Output: {divisors_count(100)}')
print('-----------Test Case 4-----------')
print('Input:  N = 1')
print(f'Output: {divisors_count(1)}')
print('-----------Test Case 5-----------')
print('Input:  N = 997')
print(f'Output: {divisors_count(997)}')