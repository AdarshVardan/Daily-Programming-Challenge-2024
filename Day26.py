def hasCycle(graph,v,visited,parent):
    visited[v]=True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            if hasCycle(graph,neighbor,visited,v):
                return True
        elif neighbor!=parent:
            return True
    return False

def detectCycle(V,E,edges):
    graph = [[] for _ in range(V)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited=[False]*V
    for i in range(V):
        if not visited[i]:
            if hasCycle(graph,i,visited,-1):
                return True
    return False


print('-----------Test Case 1-----------')
V1,E1=5,5
edges1 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
print(f'Input: V={V1},E={E1},Edges={edges1}')
print(f'Output: {detectCycle(V1,E1,edges1)}')
print('-----------Test Case 2-----------')
V2,E2=3,2
edges2 = [[0, 1], [1, 2]]
print(f'Input: V={V2},E={E2},Edges={edges2}')
print(f'Output: {detectCycle(V2,E2,edges2)}')
print('-----------Test Case 3-----------')
V3,E3=1,0
edges3 = []
print(f'Input: V={V3},E={E3},Edges={edges3}')
print(f'Output: {detectCycle(V3,E3,edges3)}')
print('-----------Test Case 4-----------')
V4,E4=4,3
edges4 = [[0, 1], [1, 2], [2, 3]]
print(f'Input: V={V4},E={E4},Edges={edges4}')
print(f'Output: {detectCycle(V4,E4,edges4)}')
