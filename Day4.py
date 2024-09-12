def swap_sort(array1,array2):
    m,n=len(array1),len(array2)
    p1,p2=m-1,0
    
    while p1>=0 and p2<n:
        if array1[p1]>array2[p2]:
            array1[p1],array2[p2]=array2[p2],array1[p1]
            p1-=1
            p2+=1
        else:
            break
    array1.sort()
    array2.sort()
    return array1,array2
    
print('-----------Test Case 1-----------')
print('Input:arr1 = [1, 3, 5], arr2 = [2, 4, 6]')
out=swap_sort([1, 3, 5],[2, 4, 6])
print(f'Output:arr1 = {out[0]}, arr2 = {out[1]}')
print('-----------Test Case 2-----------')
print('Input:arr1 = [10, 12, 14], arr2 = [1, 3, 5]')
out=swap_sort([10, 12, 14],[1, 3, 5])
print(f'Output:arr1 = {out[0]}, arr2 = {out[1]}')
print('-----------Test Case 3-----------')
print('Input:arr1 = [2, 3, 8], arr2 = [4, 6, 10]')
out=swap_sort([2, 3, 8],[4, 6, 10])
print(f'Output:arr1 = {out[0]}, arr2 = {out[1]}')
print('-----------Test Case 4-----------')
print('Input:arr1 = [1], arr2 = [2]')
out=swap_sort([1],[2])
print(f'Output:arr1 = {out[0]}, arr2 = {out[1]}')
print('-----------Test Case 5-----------')
print('Input:arr1 = [1, 2, 3, 4, ..., 50001], arr2 = [50001, ..., 100000]')
out=swap_sort(list(range(1,50001)),list(range(50001,1000001)))
print(f'Output:arr1 = {out[0][:10]}, arr2 = {out[1][:10]}')


    