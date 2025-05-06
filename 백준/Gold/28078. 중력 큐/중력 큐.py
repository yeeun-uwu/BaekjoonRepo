import sys as s
from collections import deque as dq

q = int(input())
queries = dq([list(s.stdin.readline().strip().split()) for _ in range(q)])

#기본 방향이 0 위가 뒤인 세로가 1 뒤집어진게 2 위가 앞인 세로가 3(=시계방향으로로)
dir = 0
que = dq([])
#공이 0 가림막이 1 
balls = 0

while queries:
    query = queries.popleft()

    #push와 rotate에서 세로일때 공이 떨어지는건 공통이니까...? 
    # 공 떨구는거는 나중에 한번에 하는걸로 하는게 좋을듯 
    # 따로 플래그 필요없이 마지막에 DIR이 홀수면(=세로) 공 떨어지게 
    if query[0] == "push":
        if query[1] == "b":
            que.appendleft(0)
            balls += 1
        else:
            que.appendleft(1)
    elif query[0] == "pop":
        if que:
            a = que.pop()
            if a == 0: balls -= 1
    elif query[0] == "rotate":
        if query[1] == 'l':
            dir += 3
        else:
            dir += 1
        dir %= 4
    elif query[0] == "count":
        if query[1] == "b":
            print(balls)
        else:
            print(len(que)-balls)

    if dir == 1:
        while que and que[-1] == 0:
            que.pop()
            balls -= 1
    if dir == 3:
        while que and que[0] == 0:
            que.popleft()
            balls -= 1