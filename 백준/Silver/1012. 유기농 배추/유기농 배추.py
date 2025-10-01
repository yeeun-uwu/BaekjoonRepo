# 지렁이......
# 어떤 배추에 지렁이가 있으면 인접 배추도 보호받음
# 인접 배추: 상하좌우
# 배추밭에 지렁이 몇 마리가 필요한지 구하기

t = int(input())
from collections import deque
import sys

def dfs(x, y):
    stack = deque()
    stack.append((x, y))
    visited[y][x] = 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    stack.append((nx, ny))
    # 이어진 한 덩어리다 찾았으면 1 반환
    return 1

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for a in range(n)]
    visited = [[0] * m for a in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                # 이미 검사 안한 곳에서 dfs 시작
                result += dfs(j, i)
                # 덩어리 개수 추가

    print(result)
# 테스트 케이스마다 결과 출력