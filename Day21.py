def insert_bottom(stack,item):
    if not stack:
        stack.append(item)
    else:
        temp=stack.pop()
        insert_bottom(stack,item)
        stack.append(temp)

def reverse_stack(stack):
    if not stack:
        return
    temp=stack.pop()
    reverse_stack(stack)
    insert_bottom(stack,temp)


print('-----------Test Case 1-----------')
stack=[3, 2, 1]
reverse_stack(stack)
print(f'Output: {stack}')
print('-----------Test Case 2-----------')
stack=[5]
reverse_stack(stack)
print(f'Output: {stack}')
print('-----------Test Case 3-----------')
stack=[-5, -10, -15]
reverse_stack(stack)
print(f'Output: {stack}')
print('-----------Test Case 4-----------')
stack=[]
reverse_stack(stack)
print(f'Output: {stack}')
print('-----------Test Case 5-----------')
stack=[3, 3, 3]
reverse_stack(stack)
print(f'Output: {stack}')

