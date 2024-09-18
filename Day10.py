from collections import defaultdict

def groupAnagrams(strs):
    anagrams=defaultdict(list)
    for s in strs:
        count=[0]*26
        for char in s:
            count[ord(char)-ord('a')]+=1
        anagrams[tuple(count)].append(s)
    return list(anagrams.values())

print('-----------Test Case 1-----------')
print('Input:strs[] = ["eat", "tea", "tan", "ate", "nat", "bat"]')
print(f'Output:{groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])}')
print('-----------Test Case 2-----------')
print('Input:strs[] = [""]')
print(f'Output:{groupAnagrams([""])}')
print('-----------Test Case 3-----------')
print('Input:strs[] = ["a"]')
print(f'Output:{groupAnagrams(["a"])}')
print('-----------Test Case 4-----------')
print('Input:strs[] = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]')
print(f'Output:{groupAnagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz"])}')
print('-----------Test Case 5-----------')
print('Input:strs[] = ["abc", "def", "ghi"]')
print(f'Output:{groupAnagrams(["abc", "def", "ghi"])}')
