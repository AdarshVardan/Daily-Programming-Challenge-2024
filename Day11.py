def permute_unique(s:str):
    def backtrack(path,used):
        if len(path)==len(s):
            result.append("".join(path))
            return
        for i in range(len(s)):
            if used[i] or (i>0 and s[i]==s[i-1] and not used[i-1]):
                continue
            used[i]=True
            path.append(s[i])
            backtrack(path,used)
            path.pop()
            used[i]=False
    s = sorted(s)
    result=[]
    used=[False]*len(s)
    backtrack([],used)
    return result

print('-----------Test Case 1-----------')
print('Input:strs[] = ["abc"]')
test_cases = ["abc"]
results = {test: permute_unique(test) for test in test_cases}
print(f'Output:{results}')
print('-----------Test Case 2-----------')
print('Input:strs[] = ["aab"]')
test_cases = ["aab"]
results = {test: permute_unique(test) for test in test_cases}
print(f'Output:{results}')
print('-----------Test Case 3-----------')
print('Input:strs[] = ["aaa"]')
test_cases = ["aaa"]
results = {test: permute_unique(test) for test in test_cases}
print(f'Output:{results}')
print('-----------Test Case 4-----------')
print('Input:strs[] = ["a"]')
test_cases = ["a"]
results = {test: permute_unique(test) for test in test_cases}
print(f'Output:{results}')
print('-----------Test Case 5-----------')
print('Input:strs[] = ["abcd"]')
test_cases = ["abcd"]
results = {test: permute_unique(test) for test in test_cases}
print(f'Output:{results}')




results
