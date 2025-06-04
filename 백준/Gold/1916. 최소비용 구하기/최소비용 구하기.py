from collections import deque as dq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, f = map(int, input().split())
    
    graph[a].append((b, f))  # a에서 b로 가는 버스와 요금금

start, end = map(int, input().split())
# 시작 도시와 도착 도시

# 데이크스트라라
inf = float('inf')
distance = [inf] * (n + 1)
distance[start] = 0 #시작도시는 0 

queue = dq([(0, start)])  # (현재 요금, 현재 도시)

while queue:
    current_cost, current_city = queue.popleft()
    
    if current_cost > distance[current_city]:
        continue  # 이미 더 작은 비용으로 방문한 경우
    
    for next_city, fare in graph[current_city]:
        new_cost = current_cost + fare
        
        if new_cost < distance[next_city]:
            distance[next_city] = new_cost
            queue.append((new_cost, next_city))

# 도착 도시까지의 최소 요금 출력
print(distance[end] if distance[end] != inf else -1)

