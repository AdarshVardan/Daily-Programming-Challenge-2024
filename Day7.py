def trap(height):
    if not height or len(height)<3:
        return 0

    left,right=0,len(height)-1
    left_max,right_max=height[left],height[right]
    trapped_water=0

    while left<right:
        if height[left]<height[right]:
            if height[left]>=left_max:
                left_max=height[left]
            else:
                trapped_water+=left_max-height[left]
            left+=1
        else:
            if height[right]>=right_max:
                right_max=height[right]
            else:
                trapped_water+=right_max-height[right]
            right-=1

    return trapped_water

print('-----------Test Case 1-----------')
print('Input:array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]')
print(f'Output:{trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])}')
print('-----------Test Case 2-----------')
print('Input:array = [4, 2, 0, 3, 2, 5]')
print(f'Output:{trap([4, 2, 0, 3, 2, 5])}')
print('-----------Test Case 3-----------')
print('Input:array = [1, 1, 1]')
print(f'Output:{trap([1, 1, 1])}')
print('-----------Test Case 4-----------')
print('Input:array = [5]')
print(f'Output:{trap([5])}')
print('-----------Test Case 5-----------')
print('Input:array = [2, 0, 2]')
print(f'Output:{trap([2, 0, 2])}')