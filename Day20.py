def sort_stack(stack):
    if not stack:
        return
    top = stack.pop()
    sort_stack(stack)
    insert(stack, top)

def insert(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return
    top = stack.pop()
    insert(stack, element)
    stack.append(top)

print('-----------Test Case 1-----------')
stack = [7, 1, 5]
sort_stack(stack)
print(f'Output: {stack}')

print('-----------Test Case 2-----------')
stack = [5]
sort_stack(stack)
print(f'Output: {stack}')

print('-----------Test Case 3-----------')
stack = [-3, 14, 8, 2]
sort_stack(stack)
print(f'Output: {stack}')

print('-----------Test Case 4-----------')
stack = []
sort_stack(stack)
print(f'Output: {stack}')

print('-----------Test Case 5-----------')
stack = [3, 3, 3]
sort_stack(stack)
print(f'Output: {stack}')
