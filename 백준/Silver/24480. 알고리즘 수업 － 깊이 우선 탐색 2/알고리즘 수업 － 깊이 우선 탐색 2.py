import sys

n, m, r = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}
for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)
#무방향그래프이므로 인접 리스트 형태로 받음

for key in graph:
    graph[key].sort()
    #내림차순으로 전부 정렬

visited = [0] * (n+1) #방문 순서 기록
cnt = 1

stack = [r]

while stack:
    now = stack.pop()
    if visited[now] == 0:
        visited[now] = cnt
        cnt += 1 #더 방문할거니까
        for j in graph[now]:
            if visited[j] == 0: # 방문안햇으면
                stack.append(j) #마저 스택에 추가해서 탐색

sys.stdout.write("\n".join(map(str, visited[1:])) + "\n")
