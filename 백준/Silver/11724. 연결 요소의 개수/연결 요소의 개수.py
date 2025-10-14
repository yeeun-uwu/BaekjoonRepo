# 무방향 그래프, 연결 요소의 개수
# 첫 줄: 정점 n 간선 개수 m

n, m = map(int, input().split())

# 간선의 양 끝점 주어진다 

import sys
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque as dq
visited = [False] * (n+1)

def dfs(start):
    stack = dq()
    stack.append(graph[start])
    visited[start] = 1

    while stack:
        v = stack.pop()
        for i in v:
            if not visited[i]:
                visited[i] = 1
                stack.append(graph[i])
    # 이어진 한 덩어리 다 찾았으면 1 반환
    return 1

result = 0
for i in range(1, n+1):
    if not visited[i]:
        result += dfs(i)
        # 덩어리 개수 추가

print(result)