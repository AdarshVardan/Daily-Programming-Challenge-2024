def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print('-----------Test Case 1-----------')
print("Input :s = \"()\"")
print(f'Output:{isValid("()")}')
print('-----------Test Case 2-----------')
print("Input :s = \"([)]\"")
print(f'Output:{isValid("([)]")}')
print('-----------Test Case 3-----------')
print("Input :s = \"[{()}]\"")
print(f'Output:{isValid("[{()}]")}')
print('-----------Test Case 4-----------')
print("Input :s = \"\"")
print(f'Output:{isValid("")}')
print('-----------Test Case 5-----------')
print("Input :s = \"{[}\"")
print(f'Output:{isValid("{[}")}')


