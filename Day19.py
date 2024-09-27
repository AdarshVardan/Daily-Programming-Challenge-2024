def solve_postfix(expression:str)->int:
    tokens=expression.split()
    stack=[]
    def int_divide(a,b):
        return int(a/b)
    valid_operators={'+','-','*','/'}
    if len(tokens)==1 and tokens[0].lstrip('-').isdigit():
        return int(tokens[0])
    for token in tokens:
        if token in valid_operators:
            if len(stack)<2:
                return "Invalid expression: not enough operands"
            b=stack.pop()
            a=stack.pop()
            if token=='+':
                stack.append(a+b)
            elif token=='-':
                stack.append(a-b)
            elif token=='*':
                stack.append(a * b)
            elif token=='/':
                if b==0:
                    return "Invalid expression: division by zero"
                stack.append(int_divide(a,b))
        elif token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            return f"Invalid expression: unsupported token '{token}'"
    if len(stack)!=1:
        return "Invalid expression: leftover operands or operators"
    return stack.pop()

print('-----------Test Case 1-----------')
print('Input: "5 6 +"')
print(f'Output: {solve_postfix("5 6 +")}')
print('-----------Test Case 2-----------')
print('Input: "3 4 2 * 1 5 - 2 3 ^ ^ / +"')
print(f'Output: {solve_postfix("3 4 2 * 1 5 - 2 3 ^ ^ / +")}')
print('-----------Test Case 3-----------')
print('Input: "-5 6 -"')
print(f'Output: {solve_postfix("-5 6 -")}')
print('-----------Test Case 4-----------')
print('Input: "15 7 1 1 + - / 3 * 2 1 1 + + -"')
print(f'Output: {solve_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -")}')
print('-----------Test Case 5-----------')
print('Input: "5"')
print(f'Output: {solve_postfix("5")}')
