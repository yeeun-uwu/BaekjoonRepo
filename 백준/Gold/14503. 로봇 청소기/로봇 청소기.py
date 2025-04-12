def calc(room: list[list[int]], x: int, y: int, p: int, cnt: int) -> int:
    if room[y][x] == 0: #청소되지 않음 
        room[y][x] = 2 #청소된건 2로 표기
        return calc(room, x, y, p, cnt+1) #숫자만 더해서 다시
    elif room[y][x] == 2: #이미 청소된 칸임 
        if any(room[ny][nx] == 0 for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)] 
            if 0 <= (ny := y + dy) < len(room) and 0 <= (nx := x + dx) < len(room[0])):
            #상하좌우 중 청소되지 않은 칸이 있다면
            while True:
                p -= 1 #반시계방향 회전이므로 -1
                if p < 0: p += 4
                if room[y+dy[p]][x+dx[p]] == 0: #해당방향 전진하면 청소안했을때
                    y += dy[p]
                    x += dx[p]
                    room[y][x] = 2
                    #청소까지 수행해서 다시 호출
                    return calc(room, x, y, p, cnt+1)
                #청소되지 않은 칸이 있는지 확인하고 while문 들어온거라 무한루프 없음

        else:
            #청소되지 않은 칸이 없다면 
            if room[y-dy[p]][x-dx[p]] != 1:
                return calc(room, x-dx[p], y-dy[p], p, cnt)
                #한칸 후진
            else:
                return cnt #후진 못하면 종료 



n, m = map(int, input().split())#
r, c, p = map(int, input().split())
#p는 position > 방향

#북, 동, 남, 서쪽 볼때 전진하면 이동하는 칸
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

room = [list(map(int, input().split())) for _ in range(n)]
#list[y][x] 형태

print(calc(room, c, r, p, 0))
