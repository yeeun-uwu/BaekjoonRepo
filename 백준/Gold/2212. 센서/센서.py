n = int(input())
k = int(input())
sensors = list(map(int, input().split()))

if k >= n: #센서볻다 기지국이많으면 걍 센서위에 다깔면됨
    print(0)
    exit(0)

sensors.sort()
gaps= []

for i in range(1, n):
    gaps.append(sensors[i] - sensors[i-1])
    # 사이 gap 계산해서 가장 큰 k개

gaps.sort(reverse=True)

# 남은 거리만 합산
print(sum(gaps[k - 1:]))