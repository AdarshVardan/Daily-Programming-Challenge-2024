from collections import defaultdict

def count_at_most_k(s,k):
    left=0
    count=0
    freq_map=defaultdict(int)
    distinct_count=0
    
    for right in range(len(s)):
        if freq_map[s[right]]==0:
            distinct_count+=1
        freq_map[s[right]]+=1
        while distinct_count>k:
            freq_map[s[left]]-=1
            if freq_map[s[left]]==0:
                distinct_count-=1
            left+=1
        count+=right-left+1
    return count

def count_substrings(s,k):
    return count_at_most_k(s,k)-count_at_most_k(s,k-1)


print('-----------Test Case 1-----------')
print('Input: s="pqpqs", k=2')
print(f'Output: {count_substrings("pqpqs", 2)}')
print('-----------Test Case 2-----------')
print('Input: s="aabacbebebe", k=3')
print(f'Output: {count_substrings("aabacbebebe", 3)}')
print('-----------Test Case 3-----------')
print('Input: s="a", k=1')
print(f'Output: {count_substrings("a", 1)}')
print('-----------Test Case 4-----------')
print('Input: s="abc", k=3')
print(f'Output: {count_substrings("abc", 3)}')
print('-----------Test Case 5-----------')
print('Input: s="abc", k=2')
print(f'Output: {count_substrings("abc", 2)}')

