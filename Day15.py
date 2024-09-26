def longest_substring(S:str)->int:
    char_set=set()
    start=0
    max_len=0
    
    for end in range(len(S)):
        while S[end] in char_set:
            char_set.remove(S[start])
            start+=1
        char_set.add(S[end])
        max_len=max(max_len,end-start+1)
    return max_len

print('-----------Test Case 1-----------')
print('Input: "abcabcbb"')
print(f'Output: {longest_substring("abcabcbb")}')
print('-----------Test Case 2-----------')
print('Input: "bbbbb"')
print(f'Output: {longest_substring("bbbbb")}')
print('-----------Test Case 3-----------')
print('Input: "pwwkew"')
print(f'Output: {longest_substring("pwwkew")}')
print('-----------Test Case 4-----------')
print('Input: "abcdefgh"')
print(f'Output: {longest_substring("abcdefgh")}')
print('-----------Test Case 5-----------')
print('Input: "a"')
print(f'Output: {longest_substring("a")}')