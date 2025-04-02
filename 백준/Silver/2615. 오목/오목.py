import sys as s

game = [list(map(int, s.stdin.readline().strip().split())) for i in range(19)]

# 오른쪽 / 아래 / 우하향 / 우상향 > 항상 지금 서치하던 인덱스가 맨 왼쪽쪽
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if game[x][y] != 0: #바둑돌이 놓여있으면
            stone = game[x][y]
            
            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0<=nx<19 and 0<=ny<19 and game[nx][ny] == stone:
                    cnt += 1
                    #연속된 갯수 추가가

                    if cnt == 5: #오목이면 육목체크 
                        if 0<=x-dx[i]<19 and 0<=y-dy[i]<19 and game[x - dx[i]][y - dy[i]] == stone:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and game[nx + dx[i]][ny + dy[i]] == stone:
                            break 

                        #육목아님>성공
                        print(stone)
                        print(x+1, y+1)
                        exit(0)

                    nx += dx[i]
                    ny += dy[i]


print(0)