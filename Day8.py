def reverseWords(s:str)->str:
    words=s.split()
    words=words[::-1]
    return ' '.join(words)

print('-----------Test Case 1-----------')
print('Input:"the sky is blue"')
print(f'Output:"{reverseWords("the sky is blue")}"')
print('-----------Test Case 2-----------')
print('Input:"hello world"')
print(f'Output:"{reverseWords("hello world")}"')
print('-----------Test Case 3-----------')
print('Input:"a good example"')
print(f'Output:"{reverseWords("a good example")}"')
print('-----------Test Case 4-----------')
print('Input:"   "')
print(f'Output:"{reverseWords("   ")}"')
print('-----------Test Case 5-----------')
print('Input:"word"')
print(f'Output:"{reverseWords("word")}"')
            
