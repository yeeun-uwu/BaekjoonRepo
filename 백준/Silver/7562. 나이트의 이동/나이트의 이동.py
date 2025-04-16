import sys as s
from collections import deque as dq

t = int(input())

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
#나이트가 움직일 수 있는 방법들(x, y)
for _ in range(t):
    l = int(s.stdin.readline().strip())
    now_x, now_y = map(int, s.stdin.readline().strip().split())
    target_x, target_y =  map(int, s.stdin.readline().strip().split())
    #입력 

    visited = [[False]*l for _ in range(l)]
    distance = [[0]*l for _ in range(l)]
    #방문 기록, 거리 계산
    q = dq([])
    q.append((now_x, now_y)) #현재위치 저장

    #bfs
    while q:
        x, y = q.popleft()

        if x == target_x and y == target_y: break

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy 
            if 0<=nx<l and 0<=ny<l and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y]+1
                #x, y에서 1번 더 이동한거니까

    print(distance[target_x][target_y])



