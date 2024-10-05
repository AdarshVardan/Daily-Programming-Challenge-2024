from collections import deque

def shortestPath(V,edges,start,end):
    graph=[[] for _ in range(V)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited=[False]*V
    distance=[-1]*V
    queue=deque([start])
    visited[start]=True
    distance[start]=0
    while queue:
        node=queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor]=True
                distance[neighbor]=distance[node]+1
                queue.append(neighbor)
                if neighbor==end:
                    return distance[neighbor]
    return -1

print('-----------Test Case 1-----------')
V1 = 5
edges1 = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start1,end1=0,4
print(f'Input: V={V1},Edges={edges1},start={start1},end={end1}')
print(f'Output: {shortestPath(V1,edges1,start1,end1)}')
print('-----------Test Case 2-----------')
V2 = 3
edges2 = [[0, 1], [1, 2]]
start2,end2=0,2
print(f'Input: V={V2},Edges={edges2},start={start2},end={end2}')
print(f'Output: {shortestPath(V2, edges2, start2, end2)}')
print('-----------Test Case 3-----------')
V3 = 4
edges3 = [[0, 1], [1, 2]]
start3,end3=2,3
print(f'Input: V={V3},Edges={edges3},start={start3},end={end3}')
print(f'Output: {shortestPath(V3,edges3,start3,end3)}')
