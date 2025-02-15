import sys
n = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

numbers.sort()

for i in numbers:
    print(i)