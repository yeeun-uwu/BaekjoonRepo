from collections import deque as dq

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    #양방향 리스트로 입력

# 부모 저장 배열
parent = [0] * (n + 1)

# BFS로 트리 탐색
queue = dq([1])

while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if parent[neighbor] == 0:  # 아직 방문하지 않은 경우
            parent[neighbor] = current
            queue.append(neighbor)

for i in range(2, n + 1):
    print(parent[i])  # 각 노드의 부모 노드 출력