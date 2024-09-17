def Prefix(strs):
    if not strs:
        return ""
    
    strs.sort()
    first=strs[0]
    last=strs[-1]
    common_prefix=[]
    
    for i in range(min(len(first),len(last))):
        if first[i]==last[i]:
            common_prefix.append(first[i])
        else:
            break
    
    return ''.join(common_prefix)

print('-----------Test Case 1-----------')
print('Input:["flower", "flow", "flight"]')
print(f'Output:{Prefix(["flower", "flow", "flight"])}')
print('-----------Test Case 2-----------')
print('Input:["dog", "racecar", "car"]')
print(f'Output:{Prefix(["dog", "racecar", "car"])}')
print('-----------Test Case 3-----------')
print('Input:["apple", "ape", "april"]')
print(f'Output:{Prefix(["apple", "ape", "april"])}')
print('-----------Test Case 4-----------')
print('Input:[""]')
print(f'Output:{Prefix([""])}')
print('-----------Test Case 5-----------')
print('Input:["alone"]')
print(f'Output:{Prefix(["alone"])}')

