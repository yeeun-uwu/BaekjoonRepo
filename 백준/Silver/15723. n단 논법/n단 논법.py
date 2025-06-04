n = int(input())

graph = [[False] * 26 for _ in range(26)]
# a > B라면 graph[a][b] = True
for i in range(n):
    a, _, b = input().split()  # a is b
    ai = ord(a) - ord('a')
    bi = ord(b) - ord('a')
    graph[ai][bi] = True

for k in range(26):
    for i in range(26):
        for j in range(26):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

#결론 판별
m = int(input())
for _ in range(m):
    a, _, b = input().split()
    ai = ord(a) - ord('a')
    bi = ord(b) - ord('a')
    print('T' if graph[ai][bi] else 'F')