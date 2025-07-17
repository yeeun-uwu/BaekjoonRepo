n, m = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(n)]

from collections import deque as dq

queue = dq()
queue.append((0, 0))  # (x, y)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 1:
                if map[nx][ny] != 0:
                    if map[nx][ny] == 1: map[nx][ny] = map[x][y] + 1
                    else: map[nx][ny] = min(map[nx][ny], map[x][y] + 1)

                if (nx, ny) not in queue:
                    queue.append((nx, ny))

bfs()
print(map[n - 1][m - 1])