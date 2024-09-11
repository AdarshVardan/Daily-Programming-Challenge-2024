def find_num(array):
    tortoise,hare=array[0],array[0]
    
    while True:
        tortoise=array[tortoise]
        hare=array[array[hare]]
        if tortoise==hare:
            break
    hare=array[0]
    while tortoise!=hare:
        tortoise=array[tortoise]
        hare=array[hare]
    return tortoise
    
print('-----------Test Case 1-----------')
print('Input Array:[1, 3, 4, 2, 2]')
print(f'Repeating number:{find_num([1, 3, 4, 2, 2])}')
print('-----------Test Case 2-----------')
print('Input Array:[3, 1, 3, 4, 2]')
print(f'Repeating number:{find_num([3, 1, 3, 4, 2])}')
print('-----------Test Case 3-----------')
print('Input Array:[1, 1]')
print(f'Repeating number:{find_num([1, 1])}')
print('-----------Test Case 4-----------')
print('Input Array:[1, 4, 4, 2, 3]')
print(f'Repeating number:{find_num([1, 4, 4, 2, 3])}')
print('-----------Test Case 5-----------')
print('Input Array:[1, 2, 3, ..., 99999, 50000]')
array=list(range(1,100000))
array.append(50000)
print(f'Repeating number:{find_num(array)}')
print('-----------User Input-----------')
array=input('Enter the input array:')
array=[int(num) for num in array]
print(f'Input Array:{array}')
print(f'Repeating number:{find_num(array)}')