def first_ele_with_k_repetations(arr,k):
    frequency={}
    for num in arr:
        frequency[num]=frequency.get(num,0)+1
    for num in arr:
        if frequency[num]==k:
            return num
    return -1
print('-----------Test Case 1-----------')
print('Input:  N = [2, 3, 4, 2, 2, 5, 5]')
print(f'Output: {first_ele_with_k_repetations([2, 3, 4, 2, 2, 5, 5],2)}')
print('-----------Test Case 2-----------')
print('Input:  N = [1, 1, 1, 1]')
print(f'Output: {first_ele_with_k_repetations([1, 1, 1, 1],1)}')
print('-----------Test Case 3-----------')
print('Input:  N = [10]')
print(f'Output: {first_ele_with_k_repetations([10],1)}')
print('-----------Test Case 4-----------')
print('Input:  N = [6, 6, 6, 6, 7, 7, 8, 8, 8]')
print(f'Output: {first_ele_with_k_repetations([6, 6, 6, 6, 7, 7, 8, 8, 8],3)}')