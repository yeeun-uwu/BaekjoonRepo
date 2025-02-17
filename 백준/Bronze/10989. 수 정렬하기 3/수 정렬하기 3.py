import sys

n = int(sys.stdin.readline().strip())
max_value = 10000

count = [0] * (max_value + 1)

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    count[num] += 1
    
for i in range(max_value + 1):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write((str(i) + "\n"))