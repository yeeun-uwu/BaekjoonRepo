#최대 25*25
n = int(input())
town = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상하좌우 
def houses(x, y):
    visited[x][y] = True
    count = 1 #현재 집 카운트

    for i in range(4): 
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n: #town에서 안벗어나면
            if not visited[nx][ny] and town[nx][ny] == 1:
                count += houses(nx, ny)
    return count
#다 더해져서 이어진 단지 수 리턴됨됨

n_l = [] #단지 리스트 
for i in range(n):
    for j in range(n):
        if town[i][j] == 1 and not visited[i][j]:
            n_l.append(houses(i, j))

print(len(n_l))
n_l.sort()
for i in n_l:
    print(i)
    
