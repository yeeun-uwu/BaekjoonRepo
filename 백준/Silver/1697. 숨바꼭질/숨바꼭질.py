# 수빈: n 동생: k
# 수빈이가 걸으면 1초에 1칸
# 수빈이가 순간이동하면 현재 위치 x에서 2x로 이동

n, k = map(int, input().split())

from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0] * 100001 # 0~100000
    visited[start] = 1

    while q:
        x, time = q.popleft()
        if x == k:
            return time
        for nx in (x-1, x+1, 2*x):
            #걷기랑 순간이동 했을 때의 좌표 
            if 0 <= nx <= 100000 and visited[nx] == 0:
                # 안 갔고 범위 안 지역에서
                visited[nx] = 1
                q.append((nx, time + 1))

print(bfs(n))