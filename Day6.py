def zero_subarrays(array):
    prefix_sum_map={}
    prefix_sum=0
    subarrays=[]
    
    prefix_sum_map[0]=[-1]
    
    for i in range(len(array)):
        prefix_sum+=array[i]
        if prefix_sum in prefix_sum_map:
            for j in prefix_sum_map[prefix_sum]:
                subarrays.append((j+1,i))
            prefix_sum_map[prefix_sum].append(i)
        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum]=[i]
    return subarrays

print('-----------Test Case 1-----------')
print('Input:array = [4, -1, -3, 1, 2, -1]')
print(f'Output:{zero_subarrays([4, -1, -3, 1, 2, -1])}')
print('-----------Test Case 2-----------')
print('Input:array = [1, 2, 3, 4]')
print(f'Output:{zero_subarrays([1, 2, 3, 4])}')
print('-----------Test Case 3-----------')
print('Input:array = [0, 0, 0]')
print(f'Output:{zero_subarrays([0, 0, 0])}')
print('-----------Test Case 4-----------')
print('Input:array = [-3, 1, 2, -3, 4, 0]')
print(f'Output:{zero_subarrays([-3, 1, 2, -3, 4, 0])}')
print('-----------Test Case 5-----------')
print('Input:array = [1, -1, 2, -2, 3, -3]* 10^4')
array=[1, -1, 2, -2, 3, -3] * 10**4
result=zero_subarrays(array)
print(f'Output:{result[:10]}......{result[-10:]}')
