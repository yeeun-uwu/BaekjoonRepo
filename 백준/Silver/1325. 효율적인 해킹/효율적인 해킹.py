import sys 
n, m = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[b].append(a)
#b를 해킹하면 a도 해킹할 수 있는 관계이므로 

def dfs(graph, s):
    visited = [False] * (n + 1)
    stack = [s]
    visited[s] = True
    count = 0
    
    while stack:
        p = stack.pop()
        count += 1
        for i in graph[p]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    
    return count

max_hack = 0
hacked = []

for i in range(1, n+1):
    hack = dfs(graph, i)
    if hack > max_hack:
        max_hack = hack
        hacked = [i]
    elif hack == max_hack:
        hacked.append(i)

print(" ".join(map(str, hacked)))
