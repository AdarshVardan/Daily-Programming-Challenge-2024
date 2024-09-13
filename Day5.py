def find_ladders(array):
    n=len(array)
    if n==0:
        return []
     
    lad=array[n-1]
    ladders=[array[n-1]]
    
    for p in range(n-1,-1,-1):
        if array[p]<array[p-1] and lad<array[p-1]:
            lad=array[p-1]
            ladders.append(array[p-1])
    ladders.reverse()
    return ladders

print('-----------Test Case 1-----------')
print('Input:array = [1, 2, 3, 4, 0]')
print(f'Output:{find_ladders([1, 2, 3, 4, 0])}')
print('-----------Test Case 2-----------')
print('Input:array = [7, 10, 4, 10, 6, 5, 2]')
print(f'Output:{find_ladders([7, 10, 4, 10, 6, 5, 2])}')
print('-----------Test Case 3-----------')
print('Input:array = [5]')
print(f'Output:{find_ladders([5])}')
print('-----------Test Case 4-----------')
print('Input:array = [100, 50, 20, 10]')
print(f'Output:{find_ladders([100, 50, 20, 10])}')
print('-----------Test Case 5-----------')
print('Input:array = [1, 2, 3, ..., 1000000]')
array=list(range(1,1000001))
print(f'Output:{find_ladders(array)}')