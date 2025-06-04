from collections import deque as dq

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 도로 입력(인접 리스트 형태로 저장)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# bfs 실행
distance = [-1] * (n + 1)
distance[x] = 0 # 시작 도시의 거리는 0

queue = dq([x])
while queue:
    current = queue.popleft()
    
    for neighbor in graph[current]:
        if distance[neighbor] == -1:  # 아직 방문하지 않은 r곳이면
            distance[neighbor] = distance[current] + 1 # 거리 업데이트
            queue.append(neighbor)

# k 거리인 도시 찾기
result = [i for i in range(1, n + 1) if distance[i] == k]

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)
    #없다면 -1 출력