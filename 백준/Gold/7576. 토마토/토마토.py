# 인접한(가로세로) 토마토는 하루가 지나면 익는다

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True                
# 모든 토마토가 익었는지 확인하는 함수

def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
                # 익은 토마토 위치를 큐에 삽입

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 토마토 익히기
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                if graph[nx][ny] == -1: pass
                # 토마토가 없는 칸은 패스
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                # 새로 익은 토마토 위치를 큐에 삽입

if check():
    print(0)
    exit(0)


bfs()
print(-1 if not check() else max(map(max, graph)) - 1)