def find_num(array):
    sum1=sum(array)
    n=len(array)+1
    sum2=n*(n+1)//2
    num=sum2-sum1
    return num

print('--------Test Case 1--------')
print('Given Array:[1, 2, 4, 5]')
print(f'Missing number:{find_num([1, 2, 4, 5])}')
print('--------Test Case 2--------')
print('Given Array:[2, 3, 4, 5]')
print(f'Missing number:{find_num([2, 3, 4, 5])}')
print('--------Test Case 3--------')
print('Given Array:[1, 2, 3, 4]')
print(f'Missing number:{find_num([1, 2, 3, 4])}')
print('--------Test Case 4--------')
print('Given Array:[1]')
print(f'Missing number:{find_num([1])}')
print('--------Test Case 5--------')
print('Given Array:[1, 2, 3, ..., 999999]')
print(f'Missing number:{find_num(list(range(1,1000000)))}')

print('--------User Input--------')
Array=input('Enter the numbers  of array:')
Array=list(int(num) for num in Array)
print(f'Given Array:{Array}')
print(f'Missing number:{find_num(Array)}')