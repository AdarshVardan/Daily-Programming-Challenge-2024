from collections import deque

def sliding_window_maximum(arr,k):
    if not arr:
        return []
    n=len(arr)
    if k==1:
        return arr
    result=[]
    dq=deque()
    for i in range(n):
        if dq and dq[0]<i-k+1:
            dq.popleft()
        while dq and arr[dq[-1]]<arr[i]:
            dq.pop()
        dq.append(i)
        if i>=k-1:
            result.append(arr[dq[0]])
    return result

print('-----------Test Case 1-----------')
print('Input: arr = [1, 5, 3, 2, 4, 6], k = 3')
print(f'Output: {sliding_window_maximum([1, 5, 3, 2, 4, 6],3)}')
print('-----------Test Case 2-----------')
print('Input: arr = [1, 2, 3, 4], k = 2')
print(f'Output: {sliding_window_maximum([1, 2, 3, 4],2)}')
print('-----------Test Case 3-----------')
print('Input: arr = [7, 7, 7, 7], k = 1')
