import sys as s

n = int(s.stdin.readline().strip())
meetings = [list(map(int, s.stdin.readline().strip().split())) for _ in range(n)]
#print(meetings)
#시작 시간을 기준으로 하되 같으면 끝나는 시간 기준으로 정렬
meetings_s = sorted(meetings, key = lambda x: (x[1], x[0]))
#print(meetings_s)

ans = 0
r = 0
for i in meetings_s:
    if i[0] >= r:
        ans += 1
        r = i[1]

print(ans)