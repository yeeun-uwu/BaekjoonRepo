from collections import deque

# 회원 수
n = int(input())
friends = {i: [] for i in range(1, n+1)}
# 친구 관계를 저장할 딕셔너리 초기

# 친구 관계 입력받기 
while True:
    a, b = map(int, input().split())
    if a!=-1 and b!=-1:
        # 입력된 친구 관계가 -1이 아닐 때까지 반복
        friends[a].append(b)
        friends[b].append(a)  # 친구 관계는 양방향이므로 양쪽 모두에 추가
    else:
        break

# 회원별로 점수 계산

def calc_scores(member):
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    queue = deque([member])
    visited[member] = True

    while queue:
        current = queue.popleft()
        for neighbor in friends[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    if not all(visited[1:]):
        return float('inf')  # 모든 회원을 방문하지 못한 경우 무한대 반환
    
    return max(distance[1:])  # 모든 회원을 방문한 경우 최대 거리를 반환

scores = []
min_score = float('inf')  # 최소 점수를 무한대로 초기화


for i in range(1, n+1):
    score = calc_scores(i)  # 각 회원에 대해 점수 계산
    scores.append(score)  # 점수를 리스트에 추가
    if score < min_score:  # 최소 점수 갱신
        min_score = score

# 최소 점수를 가진 사람들 찾기
candidates = [i + 1 for i, s in enumerate(scores) if s == min_score]

# 출력
print(min_score, len(candidates))
print(' '.join(map(str, candidates)))