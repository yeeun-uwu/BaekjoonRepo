n, m = map(int, input().split())
#지도 크기 

import sys 
map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
#지도 입력 받기

# 결과 배열: -1로 초기화 (나중에 0과 구분 위해)
distance = [[-1] * m for _ in range(n)]

# target 찾기 
for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            target = (i, j)
            break

# BFS를 위한 큐 초기화
from collections import deque
queue = deque()
queue.append(target)
distance[target[0]][target[1]] = 0  # 시작 위치의 거리는 0

#4방향 이동 추가
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()  # 현재 위치

    for i in range(4):  # 4방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 체크 및 이동 가능 여부 확인
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 1 and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1  # 거리 업데이트
            queue.append((nx, ny))  # 큐에 추가

# 결과 출력
for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            print(0, end=' ')       # 원래 갈 수 없는 곳
        elif distance[i][j] == -1:
            print(-1, end=' ')      # 갈 수 있었지만 도달 못한 곳
        else:
            print(distance[i][j], end=' ')  # 이동 가능한 경우 거리 출력
    print()  # 줄바꿈