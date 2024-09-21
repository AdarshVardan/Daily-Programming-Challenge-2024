def longest_palindrom(s:str)->str:
    def expand_from_center(left:int,right:int)->str:
        while left>= 0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    
    if len(s)==0:
        return ""
    if len(s)==1:
        return s
    
    longest_palindrome=""
    for i in range(len(s)):
        odd_palindrome=expand_from_center(i,i)
        if len(odd_palindrome)>len(longest_palindrome):
            longest_palindrome=odd_palindrome
        even_palindrome=expand_from_center(i,i+1)
        if len(even_palindrome)>len(longest_palindrome):
            longest_palindrome=even_palindrome
    return longest_palindrome

print('-----------Test Case 1-----------')
print('Input: "babad"')
print(f'Output: "{longest_palindrom("babad")}"')
print('-----------Test Case 2-----------')
print('Input: "cbbd"')
print(f'Output: "{longest_palindrom("cbbd")}"')
print('-----------Test Case 3-----------')
print('Input: "a"')
print(f'Output: "{longest_palindrom("a")}"')
print('-----------Test Case 4-----------')
print('Input: "aaaa"')
print(f'Output: "{longest_palindrom("aaaa")}"')
print('-----------Test Case 5-----------')
print('Input: "abc"')
print(f'Output: "{longest_palindrom("abc")}"')

