def sort(*array):
    array=list(array)
    n=len(array)
    low,mid,high=0,0,n-1
        
    while mid<=high:
        if array[mid]==0:
            array[low],array[mid]=array[mid],array[low]
            low+=1
            mid+=1
        elif array[mid]==1:
            mid+=1
        elif array[mid]==2:
            array[mid],array[high]=array[high],array[mid]
            high-=1
        else:
            print('Invaild Input')      
    return array

print('---------Test Case-1---------')    
print('Sort array:[0, 1, 2, 1, 0, 2, 1, 0]')
print(f'Sorted array:{sort(0, 1, 2, 1, 0, 2, 1, 0)}')
print('---------Test Case-2---------')    
print('Sort array:[2, 2, 2, 2]')
print(f'Sorted array:{sort(2, 2, 2, 2)}')
print('---------Test Case-3---------')    
print('Sort array:[0, 0, 0, 0]')
print(f'Sorted array:{sort(0, 0, 0, 0)}')
print('---------Test Case-4---------')    
print('Sort array:[1, 1, 1, 1]')
print(f'Sorted array:{sort(1, 1, 1, 1)}')
print('---------Test Case-5---------')    
print('Sort array:[2, 0, 1]')
print(f'Sorted array:{sort(2, 0, 1)}')
print('---------Test Case-6---------')    
print('Sort array:[]')
print(f'Sorted array:{sort()}')

print('---------User Input---------')    
array=input('Enter your array(use 0,1 and 2 numbers only):')
array=tuple(int(num) for num in array)
print(f'Sorted array:{sort(*array)}')
