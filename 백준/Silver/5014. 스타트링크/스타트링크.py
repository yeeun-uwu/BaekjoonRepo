f, s, g, u, d  = map(int, input().split())
# f: 총 층수, s: 시작 층, g: 목표 층, u: 위로 이동하는 층 수, d: 아래로 이동하는 층 수

from collections import deque as dq # deque를 사용하여 BFS 구현

def bfs(s):
    visited = [False] * (f + 1)  # 방문 여부를 저장하는 리스트
    queue = dq([(s, 0)])  # (현재 층, 이동 횟수)
    visited[s] = True  # 시작 층 방문 표시

    while queue:
        current, moves = queue.popleft()  # 현재 층과 이동 횟수 가져오기

        if current == g:  # 목표 층에 도달한 경우
            return moves  # 이동 횟수 리턴턴

        # 위로 이동
        up = current + u
        if up <= f and not visited[up]:  # 위로 이동 가능한 층인지 확인
            visited[up] = True  # 방문 표시
            queue.append((up, moves + 1))  # 큐에 추가
        
        # 아래로 이동
        down = current - d
        if down >= 1 and not visited[down]:  # 아래로 이동 가능한 층인지 확인
            visited[down] = True  # 방문 표시
            queue.append((down, moves + 1))  # 큐에 추가
    
    return -1  # 목표 층에 도달할 수 없는 경우 -1 반환

result = bfs(s)  # BFS 실행
if result == -1:
    print("use the stairs")  # 목표 층에 도달할 수 없는 경우
else:
    print(result)